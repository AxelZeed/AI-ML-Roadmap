import csv
import json
from dataclasses import asdict
from pathlib import Path

from src.models import ExperimentResult


def save_results(
    results: list[ExperimentResult],
    file_path: str | Path,
) -> None:
    output_path = Path(file_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    result_dicts = [
        asdict(result)
        for result in results
    ]

    with output_path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            result_dicts,
            file,
            indent=4,
        )


def append_results_to_csv(
    results: list[ExperimentResult],
    file_path: str | Path,
) -> None:
    output_path = Path(file_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    fieldnames = [
        "run_id",
        "name",
        "score",
        "duration_seconds",
        "started_at",
        "finished_at",
        "status",
    ]

    file_exists = output_path.exists()

    with output_path.open(
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

        for result in results:
            writer.writerow(
                {
                    "run_id": result.run_id,
                    "name": result.name,
                    "score": result.score,
                    "duration_seconds": (
                        result.duration_seconds
                    ),
                    "started_at": result.started_at,
                    "finished_at": result.finished_at,
                    "status": result.status,
                }
            )

def save_run_result(
    result: ExperimentResult,
    run_directory: str | Path,
) -> Path:
    directory = Path(
        run_directory
    )

    directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    result_file = (
        directory
        / "result.json"
    )

    with result_file.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            asdict(result),
            file,
            indent=4,
        )

    return result_file