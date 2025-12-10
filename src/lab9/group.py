import csv
from pathlib import Path
from typing import List, Dict, Any
from src.lab8.models import Student


class Group:
    """Класс для управления группой студентов в CSV-хранилище."""

    def __init__(self, storage_path: str):
        """
        Инициализация группы.

        Args:
            storage_path: путь к CSV-файлу с данными студентов
        """
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None:
        """
        Создаёт файл с заголовком, если его ещё нет.
        """
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
                writer.writeheader()

    def _read_all(self) -> List[Dict[str, str]]:
        """
        Читает все записи из CSV-файла.

        Returns:
            Список словарей с данными студентов
        """
        rows = []
        if not self.path.exists():
            return rows

        with open(self.path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)
        return rows

    def _write_all(self, rows: List[Dict[str, str]]) -> None:
        """
        Записывает все записи в CSV-файл.

        Args:
            rows: список словарей с данными студентов
        """
        with open(self.path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(rows)

    def list(self) -> List[Student]:
        """
        Возвращает всех студентов в виде объектов Student.

        Returns:
            Список объектов Student
        """
        rows = self._read_all()
        students = []

        for row in rows:
            try:
                student = Student(
                    fio=row['fio'],
                    birthdate=row['birthdate'],
                    group=row['group'],
                    gpa=float(row['gpa'])
                )
                students.append(student)
            except Exception as e:
                print(f"Ошибка при чтении студента {row}: {e}")
                continue

        return students

    def add(self, student: Student) -> bool:
        """
        Добавляет нового студента в CSV.

        Args:
            student: объект Student для добавления

        Returns:
            True если добавление успешно, False в противном случае
        """
        try:
            rows = self._read_all()

            # Проверяем, нет ли уже студента с таким ФИО
            for row in rows:
                if row['fio'] == student.fio:
                    print(f"Студент с ФИО '{student.fio}' уже существует")
                    return False

            # Добавляем нового студента
            new_row = {
                'fio': student.fio,
                'birthdate': student.birthdate,
                'group': student.group,
                'gpa': str(student.gpa)
            }
            rows.append(new_row)

            self._write_all(rows)
            return True

        except Exception as e:
            print(f"Ошибка при добавлении студента: {e}")
            return False

    def find(self, substr: str) -> List[Student]:
        """
        Находит студентов по подстроке в ФИО.

        Args:
            substr: подстрока для поиска в поле fio

        Returns:
            Список объектов Student, содержащих подстроку в ФИО
        """
        all_students = self.list()
        result = []

        for student in all_students:
            if substr.lower() in student.fio.lower():
                result.append(student)

        return result

    def remove(self, fio: str) -> bool:
        """
        Удаляет запись(и) с данным ФИО.

        Args:
            fio: ФИО студента для удаления

        Returns:
            True если удаление успешно, False в противном случае
        """
        rows = self._read_all()
        initial_length = len(rows)

        # Удаляем все записи с заданным ФИО
        rows = [row for row in rows if row['fio'] != fio]

        if len(rows) < initial_length:
            self._write_all(rows)
            return True

        print(f"Студент с ФИО '{fio}' не найден")
        return False

    def update(self, fio: str, **fields) -> bool:
        """
        Обновляет поля существующего студента.

        Args:
            fio: ФИО студента для обновления
            **fields: поля для обновления (fio, birthdate, group, gpa)

        Returns:
            True если обновление успешно, False в противном случае
        """
        rows = self._read_all()
        updated = False

        for row in rows:
            if row['fio'] == fio:
                # Обновляем указанные поля
                for field, value in fields.items():
                    if field == 'gpa':
                        row[field] = str(float(value))
                    else:
                        row[field] = str(value)
                updated = True
                break

        if updated:
            self._write_all(rows)
            return True

        print(f"Студент с ФИО '{fio}' не найден")
        return False

    def stats(self) -> Dict[str, Any]:
        """
        Собирает статистику по группе.

        Returns:
            Словарь со статистикой:
            {
                "count": общее количество студентов,
                "min_gpa": минимальный gpa,
                "max_gpa": максимальный gpa,
                "avg_gpa": средний gpa,
                "groups": распределение по группам,
                "top_5_students": топ-5 студентов по gpa
            }
        """
        students = self.list()

        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": []
            }

        # Собираем статистику
        gpa_values = [s.gpa for s in students]

        # Распределение по группам
        groups_dict = {}
        for s in students:
            if s.group not in groups_dict:
                groups_dict[s.group] = 0
            groups_dict[s.group] += 1

        # Топ-5 студентов по GPA
        sorted_students = sorted(students, key=lambda x: x.gpa, reverse=True)
        top_5 = [
            {"fio": s.fio, "gpa": s.gpa}
            for s in sorted_students[:5]
        ]

        return {
            "count": len(students),
            "min_gpa": min(gpa_values),
            "max_gpa": max(gpa_values),
            "avg_gpa": sum(gpa_values) / len(gpa_values),
            "groups": groups_dict,
            "top_5_students": top_5
        }