from pydantic_settings import BaseSettings, SettingsConfigDict
from aiobotocore.session import get_session


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_IDS: str

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_SCHEMA: str

    ENDPOINT_S3: str
    BUCKET_NAME: str

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
    
    @property
    async def s3_client(self):
        return get_session().create_client('s3', endpoint_url=self.ENDPOINT_S3)
    
    @property
    def s3_bucket(self) -> str:
        return self.BUCKET_NAME
    
    model_config = SettingsConfigDict(env_file='.env')


settings: Settings = Settings()