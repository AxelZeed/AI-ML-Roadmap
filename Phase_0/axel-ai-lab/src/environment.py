import os

from dotenv import load_dotenv


load_dotenv()


def get_environment_mode() -> str:
    return os.getenv(
        "AXEL_AI_LAB_MODE",
        "development",
    )


def get_api_key() -> str | None:
    return os.getenv(
        "AXEL_AI_LAB_API_KEY"
    )