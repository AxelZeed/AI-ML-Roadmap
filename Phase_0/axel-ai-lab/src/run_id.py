from datetime import datetime
from uuid import uuid4


def generate_run_id() -> str:
    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    random_suffix = uuid4().hex[:6]

    return (
        f"run_{timestamp}_"
        f"{random_suffix}"
    )