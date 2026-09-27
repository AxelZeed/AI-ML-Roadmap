from dataclasses import dataclass


@dataclass
class Experiment:
    name: str
    sample_count: int
    iterations: int
    enabled: bool


@dataclass
class ExperimentResult:
    run_id: str
    name: str
    score: float
    duration_seconds: float
    started_at: str
    finished_at: str
    status: str