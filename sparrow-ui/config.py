import os


class Settings:
    # sparrow_key: str = os.environ()
    api_url: str = os.environ.get("API_URL")
    huggingface_key: str = os.environ.get("HUGGINGFACE_KEY")


settings = Settings()
