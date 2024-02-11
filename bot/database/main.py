from config_data.config import db_settings

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import DeclarativeBase


class Database:

    def __init__(self) -> None:
        self.__engine: AsyncEngine = create_async_engine(db_settings.database_url)
        session = async_sessionmaker(bind=self.__engine)
        self.__session: AsyncSession = session()

    @property
    def engine(self) -> AsyncEngine:
        return self.__engine
    
    @property
    def session(self) -> AsyncSession:
        return self.__session
    

class Base(DeclarativeBase):
    pass


database: Database = Database()