from icecream import ic

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from config_db import *


class DBAPP:

    DB_HOST: str = DB_HOST
    DB_PORT: str = DB_PORT
    DB_USER: str = DB_USER
    DB_PASS: str = DB_PASS
    DB_NAME: str = DB_NAME
    DB_SQLite: str = DB_SQLite
    DB_DBMS: str = DB_DBMS
    DB_ECHO: str = DB_ECHO

    def get_async_dsn(self) -> str:
        """Метод для получения строки асинхронного подключения из .env
        :return: строку асинхронного подключения (str)
        """

        driver = ""
        db_params = f"{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        match self.DB_DBMS:
            case 'MYSQL':
                driver = f"mysql+aiomysql://"
            case 'PGSQL':
                driver = f"postgresql+asyncpg://"
            case 'SQLite':
                driver = f"sqlite+aiosqlite://"
                db_params = f"/{self.DB_SQLite}"
        dsn_self = f"{driver}{db_params}"
        ic(dsn_self)
        return dsn_self

    def get_async_engine(self, is_echo: bool) -> AsyncEngine:
        """
        Функция запуска главного движка sql/подключения синхронно
        :dsn_db: принимает в себя строку подключения
        :is_echo: включения/отключения транслирования команд SQL генерируемых sqlalchemy в консоль
        :return: возвращает экземпляр класса Engine из sqlalchemy.engine.base
        """
        engine = create_async_engine(
            url=self.get_async_dsn(),
            echo=is_echo
        )
        return engine

    def get_async_sessionmaker(self, is_echo: bool) -> async_sessionmaker:
        return async_sessionmaker(self.get_async_engine(is_echo), expire_on_commit=False)
