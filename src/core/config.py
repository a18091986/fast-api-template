from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class ServerConfig(BaseModel):
    port: int = 1234
    host: str = "0.0.0.0"


class ApiV1PrefixConfig(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"


class ApiPrefixConfig(BaseModel):
    prefix: str = "/api"
    v1: ApiV1PrefixConfig = ApiV1PrefixConfig()

class DatabaseConfig(BaseModel):
    url: str = os.getenv("APP_CONFIG__DB__URL")
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 20

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    server: ServerConfig = ServerConfig()
    api: ApiPrefixConfig = ApiPrefixConfig()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()

# if __name__ == "__main__":
#     print(settings.model_dump_json(indent=4))
