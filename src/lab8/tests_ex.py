import sys
import os

# Добавляем путь к src для импорта модулей
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.lab8.models import Student
from src.lab8.serialize import students_to_json, students_from_json


def main():
    print("=== Лабораторная работа 8 - Демонстрация ===")
    print()

    # 1. Демонстрация создания объектов
    print("1. Создание объектов Student:")
    print("-" * 40)

    student1 = Student("Иванов Иван Иванович", "2000-05-15", "SE-01", 4.7)
    student2 = Student("Петрова Анна Сергеевна", "2001-08-22", "SE-02", 3.8)
    student3 = Student("Сидоров Алексей Петрович", "1999-12-10", "SE-01", 4.2)

    print("Созданные студенты:")
    print(f"  • {student1}")
    print(f"  • {student2}")
    print(f"  • {student3}")
    print()

    # 2. Демонстрация методов
    print("2. Демонстрация методов:")
    print("-" * 40)

    print(f"Студент {student1.fio.split()[1]} является отличником: {student1.is_excellent()}")
    print(f"Студент {student2.fio.split()[1]} является отличником: {student2.is_excellent()}")
    print()

    # 3. Сериализация в JSON
    print("3. Сериализация в JSON:")
    print("-" * 40)

    students_list = [student1, student2, student3]
    output_path = "../data/lab8/students_output.json"

    # file = open("../lab4/input.txt", 'w', encoding='utf-8')

    students_to_json(students_list, output_path)
    print(f" Список студентов сохранен в: {output_path}")
    print()

    # 4. Десериализация из JSON
    print("4. Десериализация из JSON:")
    print("-" * 40)

    input_path = "../data/lab8/students_input.json"
    loaded_students = students_from_json(input_path)

    print(f" Загружено студентов из {input_path}: {len(loaded_students)}")
    for i, student in enumerate(loaded_students, 1):
        print(f"  {i}. {student}")
    print()

    # 5. Демонстрация обработки ошибок
    print("5. Демонстрация обработки ошибок:")
    print("-" * 40)

    print("Попытка создания студента с неправильным GPA (6.0):")
    try:
        bad_student1 = Student("Тестовый Студент", "2000-01-01", "SE-01", 6.0)
    except ValueError as e:
        print(f"   Ошибка: {e}")

    print("Попытка создания студента с неправильным форматом даты:")
    try:
        bad_student2 = Student("Тестовый Студент", "2000/01/01", "SE-01", 4.0)
    except ValueError as e:
        print(f"   Ошибка: {e}")

    print("Попытка создания студента с неправильным ФИО:")
    try:
        bad_student3 = Student("Студент123", "2000-01-01", "SE-01", 4.0)
    except ValueError as e:
        print(f"   Ошибка: {e}")

    print()
    print("=== Демонстрация завершена ===")


if __name__ == "__main__":
    main()