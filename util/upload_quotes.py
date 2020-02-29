import asyncio
from db.init import connect
from db.models import Quote
from config.config import Config


async def main():
    config = Config()
    db = await connect(config.db_user, config.db_pwd, config.db_name, config.db_host)

    f = open("../data/quotes")

    for i in f.readlines():
        s = i.replace("\n", "")
        s_split = s.split(";")

        quote = Quote(s_split[0], s_split[1])

        await db.set_quote_to_db(quote)

    f.close()
    await db.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
