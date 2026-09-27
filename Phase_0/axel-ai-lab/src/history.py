import csv
from pathlib import Path


def load_history(
    file_path: str | Path,
) -> list[dict[str, str]]:
    path = Path(file_path)

    history = []

    with path.open(
        "r",
        newline="",
        encoding="utf-8",
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            history.append(row)

    return history