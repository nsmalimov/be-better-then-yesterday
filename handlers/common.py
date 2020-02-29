from util.buttons import buttons_all


async def handler_common_request(user_id, db):
    records = await db.get_records_by_user_id(user_id)

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
