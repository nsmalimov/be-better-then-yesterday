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
    elif command == ButtonType.OPPORTUNITIES.value:
        text = "Я умею присылать мотивирующие цитаты."
        response = {
            "response": {
                "text": text,
                "buttons": buttons,
                "end_session": False
            },
        }

        return response
    elif command == ButtonType.HELP.value:
        text = "Данный навык позволяет получать случайные мотивирующие цитаты по запросу пользователя.\n\n" \
               "Для того, чтобы получить цитату, выберите команду \"Мотивирующая цитата\" - вы можете ввести её нажав соответствующую кнопку или введя" \
               " команду голосом. \n" \
               "Цитаты выбираются случайно из заранее загруженных в навык. Цитаты взяты из открытых источников и так или иначе" \
               " связаны с темами успеха и мотивации \n" \
               "Количество цитат, которые вы можете получить в рамках сессии не ограничено, но всего их 30\n\n" \
               "Кроме того, вы можете узнать о возможностях навыка выбрав команду \"Возможности\"\n\n" \
               "Также, вы можете узнать завершить работу с навыком выбрав команду \"Завершить\"\n\n" \
               "Команда \"Помощь\" покажет это же сообщение\n"
        response = {
            "response": {
                "text": text,
                "buttons": buttons,
                "end_session": False
            },
        }

        return response
    elif command == ButtonType.BAD.value:
        return {}
    elif command == ButtonType.GOOD.value:
        return {}
