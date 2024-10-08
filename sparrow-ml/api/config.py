from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    huggingface_key: str = os.environ.get("HF_TOKEN")
    sparrow_key: str = ""
    processor: str = "mousserlane/sb-donut-receipt-parser-v1"
    model: str = "mousserlane/sb-donut-receipt-parser-v1"
    dataset: str = "mousserlane/sb-donut-receipt-parser-v1"
    base_config: str = "naver-clova-ix/donut-base"
    base_processor: str = "naver-clova-ix/donut-base"
    base_model: str = "naver-clova-ix/donut-base"
    inference_stats_file: str = "data/donut_inference_stats.json"
    training_stats_file: str = "data/donut_training_stats.json"
    evaluate_stats_file: str = "data/donut_evaluate_stats.json"


settings = Settings()
