from db.models import ButtonType

button_commands = [
    ButtonType.GOOD.value, ButtonType.BAD.value, ButtonType.QUOTE.value, ButtonType.END.value,
]

buttons = [
    # {
    #     "title": ButtonType.GOOD.value,
    #     "hide": True
    # },
    # {
    #     "title": ButtonType.BAD.value,
    #     "hide": True
    # },
    {
        "title": ButtonType.QUOTE.value,
        "hide": True
    },
    {
        "title": ButtonType.END.value,
        "hide": True
    }
]
