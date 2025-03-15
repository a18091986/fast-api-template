from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class ServerConfig(BaseModel):
    port: int = 1234
    host: str = "0.0.0.0"


class ApiPrefixConfig(BaseModel):
    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    url: str = os.getenv("APP_CONFIG__DB__URL")
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 20


class Settings(BaseSettings):
    server: ServerConfig = ServerConfig()
    api_prefix: ApiPrefixConfig = ApiPrefixConfig()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()

# if __name__ == "__main__":
#     print(settings.model_dump_json(indent=4))
