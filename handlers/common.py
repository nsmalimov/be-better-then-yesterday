from db.models import Record, RecordTypes
from db.models import UserStatuses
from datetime import date


def count_days_before_date(date_before):
    d1 = date.today()
    d0 = date_before
    delta = d1 - d0

    return delta.days


async def handler_common_request_with_stats(user_id, db):
    records = await db.get_records_by_user_id_all(user_id)

    text = "С возвращением. "

    if len(records) == 0:
        text += "Вы пока не рассказывали о своих успехах и неудачах. Расскажите о них, чтобы я могла их записать."
    else:
        count_good, count_bad = count_good_count_bad(records)

        text += "Сегодня вы уже добавили {} хорошего и {} плохого. Произошло ли что-то еще? Если да, то скажи. Если хочешь цитатку, то шепни мне на ушко.".format(
            count_good, count_bad)

    response = {
        "response": {
            "text": text,
            "end_session": False
        },
    }

    return response


def count_good_count_bad(records):
    count_good = 0
    count_bad = 0

    added_good = {}
    added_bad = {}

    for record in records:
        if record.type == RecordTypes.BAD.value and not record.text in added_bad:
            added_bad[record.text] = 1
            count_bad += 1
        else:
            added_good[record.text] = 1

            if not record.text in added_bad:
                count_good += 1

    return count_good, count_bad


async def handler_good_bad_request(user_id, tokenized_text, record_type, db, config):
    response = {
        "response": {
            "end_session": False
        },
    }

    records = await db.get_records_by_user_id_today(user_id)

    count_repeat = 0

    count_days_before_date_arr = []

    if record_type == RecordTypes.BAD.value:
        for record in records:
            if record.text == tokenized_text:
                count_repeat += 1

                count_days_before_date_arr.append(count_days_before_date(record.created_at.date()))

    if count_repeat != 0:
        text = "Блин, это плохо, я могу ошибаться, но кажется вы уже совершали ранее эту ошибку. " \
               "А если быть точным, то {} раз, а последний раз вы ее совершали ".format(count_repeat)

        if min(count_days_before_date_arr) == 0:
            text += "сегодня ..."
        elif min(count_days_before_date_arr) == 1:
            text += "вчера ..."
        else:
            text += "{} дней назад.".format(min(count_days_before_date_arr))

        response["response"]["text"] = text
        return response

    count_good, count_bad = count_good_count_bad(records)

    if count_good >= config.max_per_day and count_bad >= config.max_per_day:
        text = "Вы уже добавили {} хорошего и {} плохого. И того и другого сегодня было достаточно. " \
               "Предлагаю взять паузу и осмыслить сегодняшний день.".format(count_good, count_bad)
    elif len(records) != 0 and count_bad >= config.max_per_day and record_type == RecordTypes.BAD.value:
        text = "Вы уже добавили {} плохого. Слишком много добавлять не очень эффективно.".format(config.max_per_day)

        if count_good != config.max_per_day:
            text += "Может было что-то хорошее?"
    elif len(records) != 0 and count_good >= config.max_per_day and record_type == RecordTypes.GOOD.value:
        text = "Вы уже добавили {} хорошего. Слишком много добавлять не очень эффективно.".format(config.max_per_day)

        if count_good != config.max_per_day:
            text += " Может было что-то плохое? Но я надеюсь, что небыло!"
    else:
        record = Record(record_type, tokenized_text, user_id)

        await db.set_record_to_db(record)

        await db.set_user_status(user_id, UserStatuses.WAIT.value)

        if record.type == RecordTypes.BAD.value:
            count_bad += 1

        if record.type == RecordTypes.GOOD.value:
            count_good += 1

        text = "Сохранила. Сегодня вы сообщили о {} случаях хорошего и {} случаях плохого.".format(count_good,
                                                                                                   count_bad)

        # больше осознанности в предложения и юмора?
        if count_good == count_bad:
            text += "\nПока что и того и другого поровну. Надеюсь, что еще чего-нибудь плохого не происходило и не произойдет."
        elif count_bad > count_good:
            text += "\nПлохого сегодня больше. Грустно, но надеюсь, что хорошего будет больше."
        #  count_bad < count_good:
        else:
            text += "\nХорошего больше. Это здорово. Так держать!"

    response["response"]["text"] = text

    return response


def handler_unknown_command():
    text = "Простите, но я вас не поняла. Повторите, пожалуйста. Если хотите узнать о том, " \
           "как со мной общаться и какие фразы я понимаю попросите помочь, скажите \"помоги\""

    response = {
        "response": {
            "text": text,
            "end_session": False
        },
    }

    return response
