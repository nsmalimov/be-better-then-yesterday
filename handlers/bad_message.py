from util.buttons import buttons_all


async def handler_bad_request():
    text = "Не надо так говорить. Давайте быль культурными."

    response = {
        "response": {
            "text": text,
            "buttons": buttons_all,
            "end_session": False
        },
    }

    return response
