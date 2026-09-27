import subprocess
import sys


def run_command(
    command: list[str],
) -> None:
    print()
    print(
        "$",
        " ".join(command),
    )
    print()

    subprocess.run(
        command,
        check=True,
    )


def main() -> None:
    print(
        "Axel AI Lab Verification"
    )
    print(
        "========================"
    )

    run_command(
        [
            sys.executable,
            "-m",
            "pytest",
            "-v",
        ]
    )

    run_command(
        [
            sys.executable,
            "-m",
            "mypy",
        ]
    )

    run_command(
        [
            sys.executable,
            "main.py",
            "--verbose",
        ]
    )

    print()
    print(
        "All verification checks passed."
    )


if __name__ == "__main__":
    main()