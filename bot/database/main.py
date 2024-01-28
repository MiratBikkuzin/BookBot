from config_data.config import settings

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):

    def __init__(self) -> None:
        self.__engine = create_async_engine(settings.database_url)
        session = async_sessionmaker(bind=self.__engine)
        self.__session = session()

    @property
    def engine(self) -> AsyncEngine:
        return self.__engine
    
    @property
    def session(self) -> AsyncSession:
        return self.__session