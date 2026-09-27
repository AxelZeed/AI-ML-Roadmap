import logging

from src.paths import LOG_DIR


def setup_logger() -> logging.Logger:
    log_file = LOG_DIR / "axel_ai_lab.log"

    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(message)s"
        ),
        handlers=[
            logging.FileHandler(
                log_file,
                encoding="utf-8",
            ),
            logging.StreamHandler(),
        ],
    )

    return logging.getLogger(
        "axel-ai-lab"
    )