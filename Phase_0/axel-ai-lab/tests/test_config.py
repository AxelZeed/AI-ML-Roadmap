from pathlib import Path

from src.config import load_experiments


def test_load_experiments_from_yaml(
    tmp_path: Path,
):
    config_file = (
        tmp_path
        / "experiments.yaml"
    )

    config_file.write_text(
        """
experiments:
  - name: test_config
    sample_count: 100
    iterations: 5
    enabled: true
""",
        encoding="utf-8",
    )

    experiments = load_experiments(
        config_file
    )

    assert len(experiments) == 1
    assert (
        experiments[0].name
        == "test_config"
    )
    assert (
        experiments[0].sample_count
        == 100
    )
    assert (
        experiments[0].iterations
        == 5
    )


def test_missing_config_returns_empty_list(
    tmp_path: Path,
):
    missing_file = (
        tmp_path
        / "missing.yaml"
    )

    experiments = load_experiments(
        missing_file
    )

    assert experiments == []