from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = f'postgresql+asyncpg://postgres:qwerty@127.0.0.1:5432/online_store_db'
    db_echo: bool = False


settings = Settings()