#!/usr/bin/env python3
"""
Простой тест для проверки структур данных.
"""

# Проверяем структуры
print("=" * 50)
print("ПРОВЕРКА STACK")
print("=" * 50)

try:
    from src.lab10.structures import Stack
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"Stack создан: {s}")
    print(f"pop(): {s.pop()}")
    print(f"pop(): {s.pop()}")
    print(f"peek(): {s.peek()}")
    print(f"Осталось элементов: {len(s)}")
    print(" Stack работает корректно")
except Exception as e:
    print(f" Ошибка в Stack: {e}")

print("\n" + "=" * 50)
print("ПРОВЕРКА QUEUE")
print("=" * 50)

try:
    from src.lab10.structures import Queue
    q = Queue()
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    print(f"Queue создана: {q}")
    print(f"dequeue(): {q.dequeue()}")
    print(f"dequeue(): {q.dequeue()}")
    print(f"peek(): {q.peek()}")
    print(f"Осталось элементов: {len(q)}")
    print(" Queue работает корректно")
except Exception as e:
    print(f" Ошибка в Queue: {e}")

print("\n" + "=" * 50)
print("ПРОВЕРКА LINKED LIST")
print("=" * 50)

try:
    from src.lab10.linked_list import SinglyLinkedList
    lst = SinglyLinkedList()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    print(f"Список создан: {lst}")
    print(f"Строковое представление: {str(lst)}")
    print(f"Количество элементов: {len(lst)}")
    print(f"Элементы: {list(lst)}")
    print(" Linked List работает корректно")
except Exception as e:
    print(f" Ошибка в Linked List: {e}")

print("\n" + "=" * 50)
print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
print("=" * 50)