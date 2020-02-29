from util.buttons import buttons_all
from db.models import Record, UserStatuses, RecordTypes
from db.models import UserStatuses


async def handler_common_request_with_stats(user_id, db):
    records = await db.get_records_by_user_id_all(user_id)

    text = "С возвращением. "

    if len(records) == 0:
        text += "Вы пока не рассказывали о своих успехах и неудачах. Расскажите о них, чтобы я могла их записать."
    else:
        for record in records:
            text += "dddd"

    response = {
        "response": {
            "text": text,
            "buttons": buttons_all,
            "end_session": False
        },
    }

    return response


async def handler_good_bad_request(user_id, text, status, db, config):
    mask = str(hash(text))

    records = await db.get_records_by_user_id_today(user_id)

    count_good = 0
    count_bad = 0

    for record in records:
        if record.type == RecordTypes.BAD.value:
            count_bad += 1
        else:
            count_good += 1

    if len(records) > config.max_per_day:
        text = "Вы уже добавили {} ".format(config.max_per_day)
    else:
        record = Record(status, text, user_id, mask)

        await db.set_record_to_db(record, mask)

        await db.set_user_status(user_id, UserStatuses.WAIT.value)

        text = "Сохранила. Сегодня вы сообщили о {} случаях хорошего и {} случаях плохого.".format(count_good, count_bad)

        # todo: добавить про то, что > <
    response = {
        "response": {
            "text": text,
            "buttons": buttons_all,
            "end_session": False
        },
    }

    return response


def handler_unknown_command():
    text = "Простите, но я вас не поняла. Повторите, пожалуйста."
    response = {
        "response": {
            "text": text,
            "buttons": buttons_all,
            "end_session": False
        },
    }

    return response
