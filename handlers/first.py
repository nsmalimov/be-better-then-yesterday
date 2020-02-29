from util.buttons import buttons_all


def handle_greeting():
    response = {
        "response": {
            "text": "Приветствую. "
                    "Рада познакомиться."
                    " Моя цель - помочь вам стать сегодня лучше, чем вы были вчера."
                    " Расскажите мне, что у вас сегодня было хорошо, а что не очень. А я запишу.",
            "buttons": buttons_all,
            "end_session": False
        },
    }

    return response
