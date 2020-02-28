from util.buttons import buttons


async def handler_common_request(user_id, db):
    records = await db.get_records_by_user_id(user_id)

    if len(records) == 0:
        text = "Вы пока не рассказывали о своих успехах и неудачах. Расскажите о них, чтобы я могла их записать."
    else:
        text = ""

        for record in records:
            text += "dddd"

    response = {
        "response": {
            "text": text,
            "buttons": buttons,
            "end_session": False
        },
    }

    return response
