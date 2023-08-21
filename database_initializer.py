import aiosqlite
from os import getenv
from dotenv import load_dotenv


async def create_database():
    load_dotenv()

    async with aiosqlite.connect(getenv("DATABASE_NAME")) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS permissions_list
            (
                id                INTEGER not null
                    primary key
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS banned_users
            (
                id                   INTEGER not null
                    primary key,
                date_banned          INTEGER(8) default (unixepoch()) not null,
                moderated_by             INTEGER not null references permissions_list,
                is_verified INTEGER not null,
                reason              TEXT not null,
                evidence             TEXT
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS ban_queue
            (
                id                   INTEGER not null
                    primary key references banned_users,
                verify_level INTEGER not null
            )
        ''')
        await db.commit()
