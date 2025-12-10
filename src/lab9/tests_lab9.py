import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / 'src'))

from src.lab8.models import Student
from src.lab9.group import Group


def main():
    print("=== Тестирование ЛР9 ===")

    # Создаем группу
    group = Group("../data/lab9/students.csv")

    # 1. Чтение существующих
    print("\n1. Существующие студенты:")
    students = group.list()
    for s in students:
        print(f"   {s.fio}, {s.birthdate}, {s.group}, {s.gpa}")

    # 2. Добавление нового
    print("\n2. Добавляем нового студента:")
    new_student = Student(
        fio="Новиков Петр Сергеевич",
        birthdate="2003-08-25",
        group="БИВТ-21-3",
        gpa=4.2
    )

    if group.add(new_student):
        print("   Добавлен!")

    # 3. Поиск
    print("\n3. Поиск 'Иванов':")
    found = group.find("Иванов")
    for s in found:
        print(f"   Найден: {s.fio}")

    # 4. Обновление
    print("\n4. Обновляем GPA Иванова:")
    if group.update("Иванов Иван Иванович", gpa=4.8):
        print("   Обновлено!")

    # 5. Удаление
    print("\n5. Удаляем Сидорова:")
    if group.remove("Сидоров Алексей Петрович"):
        print("   Удалено!")

    # 6. Статистика
    print("\n6. Статистика:")
    stats = group.stats()
    print(f"   Всего студентов: {stats['count']}")
    print(f"   Минимальный GPA: {stats['min_gpa']}")
    print(f"   Максимальный GPA: {stats['max_gpa']}")
    print(f"   Средний GPA: {stats['avg_gpa']:.2f}")
    print(f"   Распределение по группам: {stats['groups']}")

    print("   Топ-5 студентов:")
    for i, student in enumerate(stats['top_5_students'], 1):
        print(f"     {i}. {student['fio']} - {student['gpa']}")

    # 7. Финальный список
    print("\n7. Финальный список:")
    for s in group.list():
        print(f"   {s.fio}, {s.birthdate}, {s.group}, {s.gpa}")


if __name__ == "__main__":
    main()