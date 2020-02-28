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
            "text": "Приветствую. Рада познакомиться. Моя цель - помочь вам стать сегодня лучше, чем вы были вчера. Выберите команду.",
            "buttons": [
                {
                    "title": "Сказать, что было хорошо",
                    "payload": {
                        "type": "good"
                    },
                    "hide": True
                },
                {
                    "title": "Сказать, что было плохо",
                    "payload": {
                        "type": "bad"
                    },
                    "hide": True
                },
                {
                    "title": "Мотивирующая цитата",
                    "payload": {
                        "type": "quote"
                    },
                    "hide": True
                }
            ],
            "end_session": False
        },
    }

    return response
