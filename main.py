from aiohttp import web
import json
import aiohttp_cors
from handlers.first import handle_first_request, handle_greeting
from handlers.common import handler_common_request
from handlers.button_press import handle_button_press
from db.init import connect
from db.models import User

# todo tts

async def main_handler(request):
    text = await request.text()
    json_text = json.loads(text)

    version = json_text["version"]
    session_id = json_text["session"]["session_id"]
    message_id = json_text["session"]["message_id"]
    user_id = json_text["session"]["user_id"]

    # temp
    json_text["session"]["new"] = True
    user_id = "800cd5a2-6005ce4f-d6b7967c-d8f6b886"
    #

    user = await request.app.db.get_user_from_db(user_id)

    print (json_text["request"])

    if "payload" in json_text["request"]:
        payload = json_text["payload"]
        response = await handle_button_press(payload, request.app.db)
    elif json_text["session"]["new"]:
        if user is None:
            user = User()
            user.id = user_id
            await request.app.db.set_user_to_db(user)

            response = handle_greeting()
        else:
            # дать инфу по прошлым ответам (хорошее, плохое, посчитать)
            response = await handler_common_request(user_id, request.app.db)
    else:
        response = await handler_common_request(user_id, request.app.db)

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

async def init_app():
    app = web.Application()
    app.db = await connect("postgres", "123", "be_better", "79.143.31.238")

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
    web.run_app(init_app())
