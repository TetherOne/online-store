from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from pydantic_settings import BaseSettings

from config import DB_USER
from config import DB_PORT
from config import DB_NAME
from config import DB_PASS


class Settings(BaseSettings):

    api_v1_prefix: str = '/api/v1'
    db_url: str = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@db-store:{DB_PORT}/{DB_NAME}'
    db_echo: bool = False


settings = Settings()


engine = create_async_engine(settings.db_url)
async_session_maker = async_sessionmaker(engine)