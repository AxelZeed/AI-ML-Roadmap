from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

CONFIG_DIR = PROJECT_ROOT / "configs"
DATASET_DIR = PROJECT_ROOT / "datasets"
EXPERIMENT_DIR = PROJECT_ROOT / "experiments"
LOG_DIR = PROJECT_ROOT / "logs"
MODEL_DIR = PROJECT_ROOT / "models"
PLOT_DIR = PROJECT_ROOT / "plots"


def ensure_project_directories() -> None:
    directories = [
        CONFIG_DIR,
        DATASET_DIR,
        EXPERIMENT_DIR,
        LOG_DIR,
        MODEL_DIR,
        PLOT_DIR,
    ]

    for directory in directories:
        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

def get_run_directory(
    run_id: str,
) -> Path:
    run_directory = (
        EXPERIMENT_DIR
        / "runs"
        / run_id
    )

    run_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    return run_directory