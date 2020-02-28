import json

buttons = [
    {
        "title": "Сказать, что было хорошо",
        "payload": json.dumps({
            "type": "good"
        }),
        "hide": True
    },
    {
        "title": "Сказать, что было плохо",
        "payload": json.dumps({
            "type": "bad"
        }),
        "hide": True
    },
    {
        "title": "Мотивирующая цитата",
        "payload": json.dumps({
            "type": "quote"
        }),
        "hide": True
    }
]
