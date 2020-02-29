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
                "text": "Досвидания! И помните - предела нет.",
                "end_session": True
            }
        }
    elif intent_key == Intents.OPPORTUNITIES.value:
        text = "Я умею записывать твои успехи и поражения в течении дня. Вести их учет и выводить статистику. " \
               "А также я умею читать суперские мотивирующие цитаты."
        response = {
            "response": {
                "text": text,
                "end_session": False
            },
        }
    elif intent_key == Intents.HELP.value:
        text = "Я умею записывать ваши успехи и поражения в течении дня. Вести их учет и выводить статистику. " \
               "А также я умею присылать мотивирующие цитаты.\n\n" \
               "Для того, чтобы получить цитату, скажите \"Мотивирующая цитата\".\n\n" \
               "Скажите \"Сказать, что было хорошего\", чтобы инициировать запись хорошего события.\n\n" \
               "Скажите \"Сказать, что было плохого\", чтобы инициировать запись плохого события.\n\n" \
               "Скажите \"Возможности\", чтобы я кратко рассказала о том, что умею.\n\n" \
               "Также, вы можете завершить работу с навыком сказав \"Завершить\".\n\n" \
               "Скажите \"Помощь\", чтобы получить это же сообщение."
        response = {
            "response": {
                "text": text,
                "end_session": False
            },
        }
    elif intent_key == Intents.BAD.value:
        await db.set_user_status(user_id, UserStatuses.SEND_BAD.value)

        text = "Скажите четко и как можно более простыми обещупотребительными словами, " \
               "какую ошибку вы сегодня совершили. А я запишу. Скажите \"Не хочу рассказывать. Это секрет!\", чтобы я перестала ждать от вас фразы."
        response = {
            "response": {
                "text": text,
                "end_session": False
            },
        }
    elif intent_key == Intents.GOOD.value:
        await db.set_user_status(user_id, UserStatuses.SEND_GOOD.value)

        text = "Скажите четко и как можно более простыми обещупотребительными словами, что было по вашему мнению " \
               "у вас хорошо. А я запишу. Скажите \"Не хочу рассказывать. Это секрет!\", чтобы я перестала ждать от вас фразы."
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
