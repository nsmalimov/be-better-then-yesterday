from db.models import Record, RecordTypes
from db.models import UserStatuses


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

    for record in records:
        if record.type == RecordTypes.BAD.value:
            count_bad += 1
        else:
            count_good += 1

    return count_good, count_bad


async def handler_good_bad_request(user_id, text, record_type, db, config):
    mask = str(hash(text))

    records = await db.get_records_by_user_id_today(user_id)

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
        record = Record(record_type, text, user_id, mask)

        await db.set_record_to_db(record, mask)

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
    response = {
        "response": {
            "text": text,
            "end_session": False
        },
    }

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
