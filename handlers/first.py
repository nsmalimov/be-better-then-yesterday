from util.buttons import buttons


def handle_first_request():
    response = {
        "response": {
            "text": "Здравствуйте! Это мы, хороводоведы.",
            "buttons": [
                {
                    "title": "Надпись на кнопке",
                    "payload": {},
                    "hide": False
                }
            ],
            "end_session": False
        },
    }

    return response


def handle_greeting():
    response = {
        "response": {
            "text": "Приветствую. "
                    "Рада познакомиться."
                    " Моя цель - помочь вам стать сегодня лучше, чем вы были вчера."
                    " У меня есть много цитат - которые помогут тебе достигнуть успеха.",
                    #" Расскажите мне, что у вас сегодня было хорошо, а что не очень. А я запишу.",
            "buttons": buttons,
            "end_session": False
        },
    }

    return response
