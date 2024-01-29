from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_IDS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_SCHEMA: str

    @property
    def bot_token(self) -> str:
        return self.BOT_TOKEN
    
    @property
    def admin_ids(self) -> list[int]:
        return list(map(int, self.ADMIN_IDS.split(',')))
    
    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @property
    def database_schema(self) -> str:
        return self.DB_SCHEMA
    
    model_config = SettingsConfigDict(env_file='.env')


settings: Settings = Settings()