from db.models import ButtonType
from util.buttons import buttons

def handle_button_press(command, db):
    if command.type == ButtonType.QUOTE:
        quote = db.get_random_quote()

        text = "К сожалению, цитаты закончились :("

        if not(quote is None):
            text = quote.text + "\n" + quote.author

        response = {
            "response": {
                "text": text,
                "buttons": buttons,
                "end_session": False
            },
        }

        return response
    elif command.type == ButtonType.BAD:
        return {}
    elif command.type == ButtonType.GOOD:
        pass
