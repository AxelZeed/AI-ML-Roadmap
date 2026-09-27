import csv
import json
from pathlib import Path

from src.models import ExperimentResult
from src.storage import (
    append_results_to_csv,
    save_results,
    save_run_result,
)


def test_save_results_creates_json_file(
    tmp_path: Path,
) -> None:
    output_file = (
        tmp_path
        / "nested"
        / "results.json"
    )

    results = [
        ExperimentResult(
            run_id="run_first",
            name="first",
            score=1.0,
            duration_seconds=0.1,
            started_at="2026-09-15T10:00:00",
            finished_at="2026-09-15T10:00:01",
            status="success",
        )
    ]

    save_results(
        results,
        output_file,
    )

    assert output_file.exists()

    data = json.loads(
        output_file.read_text(
            encoding="utf-8"
        )
    )

    assert len(data) == 1
    assert data[0]["name"] == "first"
    assert (
        data[0]["run_id"]
        == "run_first"
    )
    assert data[0]["score"] == 1.0
    assert (
        data[0]["status"]
        == "success"
    )


def test_append_results_to_csv_creates_history(
    tmp_path: Path,
) -> None:
    history_file = (
        tmp_path
        / "history"
        / "history.csv"
    )

    results = [
        ExperimentResult(
            run_id="run_second",
            name="second",
            score=2.0,
            duration_seconds=0.2,
            started_at="2026-09-15T10:01:00",
            finished_at="2026-09-15T10:01:01",
            status="success",
        )
    ]

    append_results_to_csv(
        results,
        history_file,
    )

    assert history_file.exists()

    with history_file.open(
        "r",
        newline="",
        encoding="utf-8",
    ) as file:
        rows = list(
            csv.DictReader(file)
        )

    assert len(rows) == 1
    assert rows[0]["name"] == "second"
    assert (
        rows[0]["run_id"]
        == "run_second"
    )
    assert (
        rows[0]["status"]
        == "success"
    )

def test_append_results_to_csv_appends_rows(
    tmp_path: Path,
) -> None:
    history_file = (
        tmp_path
        / "history.csv"
    )

    first_results = [
        ExperimentResult(
            run_id="run_first",
            name="first",
            score=1.0,
            duration_seconds=0.1,
            started_at="2026-09-15T10:00:00",
            finished_at="2026-09-15T10:00:01",
            status="success",
        )
    ]

    second_results = [
        ExperimentResult(
            run_id="run_second",
            name="second",
            score=2.0,
            duration_seconds=0.2,
            started_at="2026-09-15T10:01:00",
            finished_at="2026-09-15T10:01:01",
            status="success",
        )
    ]

    append_results_to_csv(
        first_results,
        history_file,
    )

    append_results_to_csv(
        second_results,
        history_file,
    )

    with history_file.open(
        "r",
        newline="",
        encoding="utf-8",
    ) as file:
        rows = list(
            csv.DictReader(file)
        )

    assert len(rows) == 2
    assert rows[0]["name"] == "first"
    assert rows[1]["name"] == "second"

def test_save_run_result_creates_result_file(
    tmp_path: Path,
) -> None:
    result = ExperimentResult(
        run_id="run_test",
        name="test",
        score=1.5,
        duration_seconds=0.1,
        started_at=(
            "2026-09-15T10:00:00"
        ),
        finished_at=(
            "2026-09-15T10:00:01"
        ),
        status="success",
    )

    run_directory = (
        tmp_path
        / result.run_id
    )

    result_file = save_run_result(
        result,
        run_directory,
    )

    assert result_file.exists()

    data = json.loads(
        result_file.read_text(
            encoding="utf-8"
        )
    )

    assert (
        data["run_id"]
        == "run_test"
    )

    assert (
        data["status"]
        == "success"
    )