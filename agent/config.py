"""Proje ayarlarını .env dosyasından güvenli biçimde yükler."""

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    llm_api_key: str
    llm_model: str
    max_steps: int = 20

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()