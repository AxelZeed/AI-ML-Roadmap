import csv


def load_history(
    file_path: str,
) -> list[dict[str, str]]:

    with open(
        file_path,
        "r",
        newline="",
        encoding="utf-8",
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            history.append(row)

    return history