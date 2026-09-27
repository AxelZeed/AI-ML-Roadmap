from src.experiment import run_experiment
from src.models import Experiment


def test_run_experiment_returns_successful_result():
    experiment = Experiment(
        name="test_experiment",
        sample_count=10,
        iterations=2,
        enabled=True,
    )

    result = run_experiment(experiment)
    assert result.run_id.startswith(
        "run_"
    )
    assert result.name == "test_experiment"
    assert result.score > 0
    assert result.duration_seconds >= 0
    assert result.started_at
    assert result.finished_at       
    assert result.status == "success"


def test_run_experiment_is_deterministic():
    experiment = Experiment(
        name="deterministic_test",
        sample_count=100,
        iterations=3,
        enabled=True,
    )

    first_result = run_experiment(experiment)
    second_result = run_experiment(experiment)

    assert first_result.score == second_result.score

def test_each_run_gets_unique_run_id():
    experiment = Experiment(
        name="unique_id_test",
        sample_count=10,
        iterations=1,
        enabled=True,
    )

    first_result = run_experiment(
        experiment
    )

    second_result = run_experiment(
        experiment
    )

    assert (
        first_result.run_id
        != second_result.run_id
    )