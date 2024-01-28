from database.models import UsersTable
from database.main import Database

from sqlalchemy import update


async def update_user_page(new_page: int, user_id: int) -> None:
    async with Database().session as session:
        stmt = (
            update(UsersTable)
            .values(page=new_page)
            .where(UsersTable.c.user_id == user_id)
        )
        await session.execute(stmt)
        await session.commit()