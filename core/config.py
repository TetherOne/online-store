from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class Settings(BaseSettings):

    api_v1_prefix: str = '/api/v1'
    db_url: str = f'postgresql+asyncpg://postgres:qwerty@127.0.0.1:5432/online_store_db'
    db_echo: bool = False


settings = Settings()

engine = create_async_engine(settings.db_url)
async_session_maker = async_sessionmaker(engine)