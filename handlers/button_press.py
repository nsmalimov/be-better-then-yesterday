from db.models import ButtonType, UserStatuses
from util.buttons import buttons_all, buttons_wait_reply


async def handle_button_press(user_id, command, db):
    if command == ButtonType.QUOTE.value:
        quote = await db.get_random_quote()

        text = "К сожалению, цитаты закончились :("

        if not (quote is None):
            text = quote.text + "\n" + quote.author

        response = {
            "response": {
                "text": text,
                "buttons": buttons_all,
                "end_session": False
            },
        }
    elif command == ButtonType.END.value:
        await db.set_user_status(user_id, UserStatuses.WAIT.value)

        response = {
            "response": {
                "text": "Досвидания! И помни - предела нет.",
                "end_session": True
            }
        }
    elif command == ButtonType.OPPORTUNITIES.value:
        text = "Я умею присылать мотивирующие цитаты."
        response = {
            "response": {
                "text": text,
                "buttons": buttons_all,
                "end_session": False
            },
        }
    elif command == ButtonType.HELP.value:
        text = "Данный навык позволяет получать случайные мотивирующие цитаты по запросу пользователя.\n\n" \
               "Для того, чтобы получить цитату, выберите команду \"Мотивирующая цитата\" - вы можете ввести её нажав соответствующую кнопку или введя" \
               " команду голосом. \n" \
               "Цитаты выбираются случайно из заранее загруженных в навык. Цитаты взяты из открытых источников и так или иначе" \
               " связаны с темами успеха и мотивации \n." \
               "Количество цитат, которые вы можете получить в рамках сессии не ограничено, но всего их 30.\n\n" \
               "Кроме того, вы можете узнать о возможностях навыка выбрав команду \"Возможности\".\n\n" \
               "Также, вы можете узнать завершить работу с навыком выбрав команду \"Завершить\".\n\n" \
               "Команда \"Помощь\" покажет это же сообщение."
        response = {
            "response": {
                "text": text,
                "buttons": buttons_all,
                "end_session": False
            },
        }
    elif command == ButtonType.BAD.value:
        await db.set_user_status(user_id, UserStatuses.SEND_BAD.value)

        text = "Скажите четко и как можно более простыми обещупотребительными словами, " \
               "какую ошибку вы сегодня совершили. А я запишу."
        response = {
            "response": {
                "text": text,
                "buttons": buttons_wait_reply,
                "end_session": False
            },
        }
    elif command == ButtonType.GOOD.value:
        await db.set_user_status(user_id, UserStatuses.SEND_GOOD.value)

        text = "Скажите четко и как можно более простыми обещупотребительными словами, что было по вашему мнению " \
               "было у вас хорошо. А я запишу."
        response = {
            "response": {
                "text": text,
                "buttons": buttons_wait_reply,
                "end_session": False
            },
        }
    # elif command == ButtonType.DONT_WANT_TELL.value:
    else:
        await db.set_user_status(user_id, UserStatuses.WAIT.value)

        text = "Ну как хотите. Хозяин-барин."
        response = {
            "response": {
                "text": text,
                "buttons": buttons_all,
                "end_session": False
            },
        }

    return response
