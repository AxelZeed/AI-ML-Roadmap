from src.comparison import (
    get_best_result,
    get_fastest_result,
    get_slowest_result,
)
from src.models import ExperimentResult


def make_result(
    name: str,
    score: float,
    duration: float,
) -> ExperimentResult:
    return ExperimentResult(
        run_id=f"run_{name}",
        name=name,
        score=score,
        duration_seconds=duration,
        started_at=(
            "2026-09-15T10:00:00"
        ),
        finished_at=(
            "2026-09-15T10:00:01"
        ),
        status="success",
    )


def test_get_best_result():
    results = [
        make_result(
            "low",
            score=1.0,
            duration=0.1,
        ),
        make_result(
            "high",
            score=5.0,
            duration=0.2,
        ),
    ]

    result = get_best_result(results)

    assert result is not None
    assert result.name == "high"


def test_get_fastest_result():
    results = [
        make_result(
            "slow",
            score=5.0,
            duration=1.0,
        ),
        make_result(
            "fast",
            score=1.0,
            duration=0.1,
        ),
    ]

    result = get_fastest_result(
        results
    )

    assert result is not None
    assert result.name == "fast"


def test_get_slowest_result():
    results = [
        make_result(
            "slow",
            score=5.0,
            duration=1.0,
        ),
        make_result(
            "fast",
            score=1.0,
            duration=0.1,
        ),
    ]

    result = get_slowest_result(
        results
    )

    assert result is not None
    assert result.name == "slow"


def test_comparison_returns_none_for_empty_results():
    results: list[ExperimentResult] = []

    assert get_best_result(
        results
    ) is None

    assert get_fastest_result(
        results
    ) is None

    assert get_slowest_result(
        results
    ) is None