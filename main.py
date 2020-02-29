from aiohttp import web
import json
import aiohttp_cors
from handlers.first import handle_greeting
from handlers.common import handler_common_request_with_stats, handler_good_bad_request, handler_unknown_command
from handlers.intents import handle_intents
from handlers.bad_message import handler_bad_request
from db.init import connect
from db.models import User, UserStatuses, RecordTypes
from config.config import Config


# todo tts

async def main_handler(request):
    text = await request.text()
    json_text = json.loads(text)

    version = json_text["version"]
    session_id = json_text["session"]["session_id"]
    message_id = json_text["session"]["message_id"]
    user_id = json_text["session"]["user_id"]

    # #
    # json_text["session"]["new"] = False
    # user_id = "d866ae29-6eb651f5-a6f881df-55e86c3e"
    # #

    user = await request.app.db.get_user_from_db(user_id)

    text = json_text["request"]["command"]

    # bad message
    if "dangerous_context" in json_text["request"]["markup"] and json_text["request"]["markup"]["dangerous_context"]:
        response = handler_bad_request()
    # good, bad, quote, end [help, responsibilities]
    elif json_text["request"]["nlu"]["intents"] != {}:
        intent_key = json_text["request"]["nlu"]["intents"].keys()[0]
        response = await handle_intents(user_id, intent_key, request.app.db) \
    # начал новую сессию
    elif json_text["session"]["new"]:
        # юзера вообще в первый раз - приветствуем
        if user is None:
            user = User()
            user.id = user_id

            await request.app.db.set_user_to_db(user)

            response = handle_greeting()
        else:
            # пользователь уже был
            # дать инфу по прошлым ответам (хорошее, плохое, посчитать)
            response = await handler_common_request_with_stats(user_id, request.app.db)
    else:
        # сессия не новая, но и не команда из списка [это хорошее и плохое]
        if user.status == UserStatuses.SEND_BAD.value:
            response = await handler_good_bad_request(user_id, text, RecordTypes.BAD.value, request.app.db, request.app.config)
        elif user.status == UserStatuses.SEND_GOOD.value:
            response = await handler_good_bad_request(user_id, text, RecordTypes.GOOD.value, request.app.db, request.app.config)
        else:
            response = handler_unknown_command()

    response["session"] = {
        "session_id": session_id,
        "message_id": message_id,
        "user_id": user_id
    }
    response["version"] = version

    response = json.dumps(response)

    return web.Response(text=response)


async def on_shutdown(app):
    await app.db.close()


async def init_app(config):
    app = web.Application()

    app.db = await connect(config.db_user, config.db_pwd, config.db_name, config.db_host)
    app.config = config

    cors = aiohttp_cors.setup(app)

    resource = cors.add(app.router.add_resource("/"))

    cors.add(
        resource.add_route("POST", main_handler), {
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                allow_headers=("*", "*"),
                max_age=3600,
            )
        })

    app.on_shutdown.append(on_shutdown)

    return app


if __name__ == '__main__':
    config = Config()

    web.run_app(init_app(config), port=config.port)
