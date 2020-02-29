from db.models import User, Quote, Record


class DB:
    def __init__(self, conn):
        self.conn = conn

    async def close(self):
        await self.conn.close()

    async def get_user_from_db(self, user_id):
        row = await self.conn.fetchrow(
            'SELECT * FROM users WHERE id = $1', user_id)

        if not (row is None):
            user = User()
            user.load_by_dict(**row)
            return user

        return None

    async def set_user_to_db(self, user):
        await self.conn.execute('''
                INSERT INTO users(id) VALUES($1)
            ''', user.id)

    async def set_quote_to_db(self, quote):
        await self.conn.execute('''
                        INSERT INTO quotes(text, author) VALUES($1, $2)
                    ''', quote.text, quote.author)

    async def get_random_quote(self):
        row = await self.conn.fetchrow('SELECT * FROM quotes ORDER BY random()')

        if not (row is None):
            quote = Quote()
            quote.load_by_dict(**row)
            return quote

        return None

    async def get_records_by_user_id(self, user_id):
        records = []

        rows = await self.conn.fetch(
            'SELECT * FROM records WHERE user_id = $1', user_id)

        if not (rows is None):
            for row in rows:
                record = Record()
                record.load_by_dict(**row)
                records.append(record)

            return records

        return None

    async def set_user_status(self, user_id, status):
        await self.conn.execute('''UPDATE users SET status = $2 WHERE id = $1''', user_id, status)
