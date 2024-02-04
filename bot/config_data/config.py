from pydantic_settings import BaseSettings, SettingsConfigDict
from aiobotocore.session import get_session
from types_aiobotocore_s3.client import S3Client


class BotSettings(BaseSettings):
    token: str
    admin_ids: str
    
    @property
    def admin_ids(self) -> list[int]:
        return list(map(int, self.ADMIN_IDS.split(',')))
    
    model_config = SettingsConfigDict(env_file='.env', env_prefix='BOT_', case_sensitive=False)


class DatabaseSettings(BaseSettings):
    host: str
    port: int
    name: str
    user: str
    password: str
    postgres_schema: str

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
    
    model_config = SettingsConfigDict(env_file='.env', env_prefix='DB_', case_sensitive=False)


class S3Settings(BaseSettings):
    endpoint: str
    bucket_name: str

    @property
    def client(self) -> S3Client:
        return get_session().create_client('s3', endpoint_url=self.endpoint)
    
    model_config = SettingsConfigDict(env_file='.env', env_prefix='S3_', case_sensitive=False)


bot_settings: BotSettings = BotSettings()
db_settings: DatabaseSettings = DatabaseSettings()
s3_settings: S3Settings = S3Settings()