import json
import csv
from pathlib import Path



def json_to_csv(json_path: str, csv_path: str) -> None:
    jp = Path(json_path)
    if jp.suffix != ".json":
        raise ValueError("Неверный тип файла")
    if not jp.exists():
        raise FileNotFoundError("Файл не найден")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if len(data) == 0:
        raise ValueError("Пустой JSON")

    all_headers = set()
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Элементы JSON должны быть словарями")
        all_headers.update(item.keys())

    headers = sorted(all_headers)

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()


        for item in data:
            row = {}
            for header in headers:
                row[header] = item.get(header, '')
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    cp = Path(csv_path)
    if cp.suffix != ".csv":
        raise ValueError("Неверный тип файла")
    if not cp.exists():
        raise FileNotFoundError("Файл не найден")

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if len(rows) == 0:
        raise ValueError("Пустой CSV")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


json_to_csv("src/data/samples/people.json", "src/data/out/people_from_json.csv")
csv_to_json("src/data/samples/people.csv", "src/data/out/people_from_csv.json")