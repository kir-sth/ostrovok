from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    FASTAPI_HOST: str
    FASTAPI_PORT: int
    PG_DB_HOST: str
    PG_DB_PORT: int
    PG_DB_USER: str
    PG_DB_PASS: str
    PG_DB_NAME: str
    PG_DB_DRIVER: str
    PG_DB_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    REDIS_HOST: str
    REDIS_PORT: int

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
