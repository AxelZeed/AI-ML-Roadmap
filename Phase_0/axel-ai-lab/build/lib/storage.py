import csv
import json
from datetime import datetime
from dataclasses import asdict
from src.models import ExperimentResult

def save_results(
    results: list[ExperimentResult],
    file_path: str,
) -> None:
    result_dicts = [asdict(result) for result in results]
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            result_dicts,
            file,
            indent=4,
        )


def append_results_to_csv(
    results: list[ExperimentResult],
    file_path: str,
    fieldnames: list[str] = ["timestamp", "name", "score"]
) -> None:

    try:
        with open(file_path, "r", encoding="utf-8"):
            file_exists = True

    except FileNotFoundError:
        file_exists = False

    with open(
        file_path,
        "a",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
        )

        if not file_exists:
            writer.writeheader()

        timestamp = datetime.now().isoformat(
            timespec="seconds"
        )

        for result in results:
            writer.writerow(
                {
                    "timestamp": timestamp,                    
                    "name": result.name,
                    "score": result.score,
                }
            )