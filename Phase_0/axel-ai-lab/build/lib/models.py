from dataclasses import dataclass


@dataclass
class Experiment:
    name: str
    learning_rate: float
    epochs: int
    enabled: bool

@dataclass
class ExperimentResult:
    name: str
    score: float