from db.models import ButtonType
from util.buttons import buttons


async def handle_button_press(command, db):
    if command == ButtonType.QUOTE.value:
        quote = await db.get_random_quote()

        text = "К сожалению, цитаты закончились :("

        if not (quote is None):
            text = quote.text + "\n" + quote.author

        response = {
            "response": {
                "text": text,
                "buttons": buttons,
                "end_session": False
            },
        }

        return response
    elif command == ButtonType.END.value:
        response = {
            "response": {
                "text": "Досвидания! И помни - предела нет.",
                "end_session": True
            }
        }
        return response
    elif command == ButtonType.BAD.value:
        return {}
    elif command == ButtonType.GOOD.value:
        return {}
