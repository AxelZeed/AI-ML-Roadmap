from pathlib import Path

from src import paths


def test_get_run_directory_creates_directory(
    tmp_path: Path,
    monkeypatch,
) -> None:
    fake_experiment_dir = (
        tmp_path
        / "experiments"
    )

    monkeypatch.setattr(
        paths,
        "EXPERIMENT_DIR",
        fake_experiment_dir,
    )

    run_directory = (
        paths.get_run_directory(
            "run_test"
        )
    )

    assert run_directory.exists()

    assert run_directory == (
        fake_experiment_dir
        / "runs"
        / "run_test"
    )