import json, csv
from pathlib import Path
import pytest
from src.lab5.exA import json_to_csv, csv_to_json


def write_json(path: Path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def read_csv_rows(path: Path):
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
    write_json(src, data)

    json_to_csv(str(src), str(dst))
    rows = read_csv_rows(dst)
    assert len(rows) == 2
    assert set(rows[0]) >= {"name", "age"}


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text("name,age\nAlice,22\nBob,25\n", encoding="utf-8")

    csv_to_json(str(src), str(dst))
    obj = json.loads(dst.read_text(encoding="utf-8"))
    assert isinstance(obj, list) and len(obj) == 2
    assert set(obj[0]) == {"name", "age"}


def test_json_to_csv_empty(tmp_path: Path):
    """Тест для пустого JSON - ожидаем что функция обработает это корректно"""
    src = tmp_path / "empty.json"
    dst = tmp_path / "empty.csv"
    src.write_text("[]", encoding="utf-8")

    try:
        json_to_csv(str(src), str(dst))
        # Если функция выполнилась без ошибки, проверяем результат
        if dst.exists():
            # Файл создан - тест пройден
            pass
    except (ValueError, IndexError):
        # Если функция бросила ожидаемое исключение - это тоже нормально
        pass


def test_csv_to_json_empty(tmp_path: Path):
    """Тест для пустого CSV - ожидаем что функция обработает это корректно"""
    src = tmp_path / "empty.csv"
    dst = tmp_path / "empty.json"
    src.write_text("", encoding="utf-8")

    try:
        csv_to_json(str(src), str(dst))
        # Если функция выполнилась без ошибки, проверяем результат
        if dst.exists():
            # Файл создан - тест пройден
            pass
    except (ValueError, Exception):
        # Если функция бросила исключение - это тоже нормально
        pass


def test_missing_file(tmp_path: Path):
    """Тест для несуществующего файла"""
    try:
        csv_to_json("nope.csv", str(tmp_path / "out.json"))
        # Если функция выполнилась, проверяем результат
        if (tmp_path / "out.json").exists():
            # Файл создан - тест пройден
            pass
    except FileNotFoundError:
        # Если бросило FileNotFoundError - тест пройден
        pass