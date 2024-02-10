from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    token: str
    admin_ids: str
    
    @property
    def admin_ids_lst(self) -> list[int]:
        return list(map(int, self.admin_ids.split(',')))
    
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