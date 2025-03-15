from pydantic import BaseModel
from pydantic_settings import BaseSettings


class ServerConfig(BaseModel):
    port: int = 1234
    host: str = "0.0.0.0"

class ApiPrefixConfig(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):
     server: ServerConfig = ServerConfig()
     api_prefix: ApiPrefixConfig = ApiPrefixConfig()

     




settings = Settings()