from functools import lru_cache
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Fairy(BaseModel):
    debug: bool


class Auth(BaseModel):
    secret_key: str


class DB(BaseModel):
    dialect: str
    user: str
    password: str
    host: str
    port: int
    database: str
    pool_size: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="__")

    fairy: Fairy
    auth: Auth
    db: DB


@lru_cache
def get_settings() -> Settings:
    return Settings.model_validate({})
