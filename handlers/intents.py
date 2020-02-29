from db.models import UserStatuses
from enum import Enum


class Intents(Enum):
    QUOTE = "quote"
    GOOD = "good"
    BAD = "bad"
    END = "end"
    HELP = "help"
    OPPORTUNITIES = "opportunities"
    DONT_WANT_TELL = "dont_want"

    STAT_ALL = "stat_all"
    STAT_DAY = "stat_day"
    STAT_MONTH = "stat_month"


async def handle_intents(user_id, intent_key, db):
    if intent_key == Intents.QUOTE.value:
        quote = await db.get_random_quote()

        text = "К сожалению, цитаты закончились :("

        if not (quote is None):
            text = quote.text + "\n" + quote.author

        response = {
            "response": {
                "text": text,
                "end_session": False
            },
        }
    elif intent_key == Intents.END.value:
        await db.set_user_status(user_id, UserStatuses.WAIT.value)

        response = {
            "response": {
                "text": "Досвидания! И помни - предела нет.",
                "end_session": True
            }
        }
    elif intent_key == Intents.OPPORTUNITIES.value:
        text = "Я умею присылать мотивирующие цитаты."
        response = {
            "response": {
                "text": text,
                "end_session": False
            },
        }
    elif intent_key == Intents.HELP.value:
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
                "end_session": False
            },
        }
    elif intent_key == Intents.BAD.value:
        await db.set_user_status(user_id, UserStatuses.SEND_BAD.value)

        text = "Скажите четко и как можно более простыми обещупотребительными словами, " \
               "какую ошибку вы сегодня совершили. А я запишу."
        response = {
            "response": {
                "text": text,
                "end_session": False
            },
        }
    elif intent_key == Intents.GOOD.value:
        await db.set_user_status(user_id, UserStatuses.SEND_GOOD.value)

        text = "Скажите четко и как можно более простыми обещупотребительными словами, что было по вашему мнению " \
               "было у вас хорошо. А я запишу."
        response = {
            "response": {
                "text": text,
                "end_session": False
            },
        }
    # elif intent_key == Intents.DONT_WANT_TELL.value:
    else:
        await db.set_user_status(user_id, UserStatuses.WAIT.value)

        text = "Ну как хотите. Хозяин-барин."
        response = {
            "response": {
                "text": text,
                "end_session": False
            },
        }

    return response
