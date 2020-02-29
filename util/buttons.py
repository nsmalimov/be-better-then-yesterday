from db.models import ButtonType

button_commands = [
    ButtonType.GOOD.value,
    ButtonType.BAD.value,
    ButtonType.QUOTE.value,
    ButtonType.END.value,
    ButtonType.HELP.value,
    ButtonType.OPPORTUNITIES.value,
    ButtonType.DONT_WANT_TELL.value
]

buttons_all = [
    {
        "title": ButtonType.GOOD.value,
        "hide": True
    },
    {
        "title": ButtonType.BAD.value,
        "hide": True
    },
    {
        "title": ButtonType.QUOTE.value,
        "hide": True
    },
    {
        "title": ButtonType.END.value,
        "hide": True
    },
    # {
    #     "title": ButtonType.HELP.value,
    #     "hide": True
    # },
    # {
    #     "title": ButtonType.OPPORTUNITIES.value,
    #     "hide": True
    # }
]

buttons_wait_reply = [
    {
        "title": ButtonType.DONT_WANT_TELL.value,
        "hide": True
    },
    {
        "title": ButtonType.END.value,
        "hide": True
    },
]