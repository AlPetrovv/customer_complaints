import os.path
import pathlib
from openai import Client

from pydantic import BaseModel, model_validator, ConfigDict
from pydantic_settings import BaseSettings, SettingsConfigDict

BASEDIR = pathlib.Path(__file__).parent

class Integration(BaseModel):
    sentiment_api_key: str
    sentiment_api_url: str
    openai_api_key: str
    openai_organization: str
    openai_project: str
    openai_model: str
    openai_client: Client

    model_config = ConfigDict( arbitrary_types_allowed=True)

    @model_validator(mode='before')
    @classmethod
    def set_field_client_if_empty(cls, data):
        if isinstance(data, dict) and data.get('openai_client') is None:
            data['openai_client'] = Client(
                api_key=data['openai_api_key'],
                organization=data['openai_organization'],
                project=data['openai_project']
            )
        return data




class ApiPrefix(BaseModel):
    complaint: str = "/complaints"

class Database(BaseModel):
    url: str
    echo: bool


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(os.path.join(BASEDIR.as_posix(), '../envs/app.env'), os.path.join(BASEDIR.as_posix(), '../envs/db.env')),
        extra='allow',
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix='APP_CONFIG__',
    )
    db: Database
    api: ApiPrefix = ApiPrefix()
    integration: Integration


settings = Settings()
