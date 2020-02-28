from db.models import User


class DB:
    def __init__(self, conn):
        self.conn = conn

    async def close(self):
        await self.conn.close()

    async def get_user_from_db(self, user_id):
        row = await self.conn.fetchrow(
            'SELECT * FROM user WHERE id = $1', user_id)

        user = User(**row)

        return user

    async def set_user_to_db(self, user):
        await self.conn.execute('''
                INSERT INTO user(id) VALUES($1)
            ''', user.id)
