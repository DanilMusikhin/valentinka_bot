from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Config(BaseSettings):
    bot_token: SecretStr
    varya_id: int
    my_id: int

    model_config = SettingsConfigDict(
        env_file= "config/config.env",
        env_file_encoding= "utf-8",
        case_sensitive= False
    )

config = Config()