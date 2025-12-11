from collections import deque
from typing import Any, Optional


class Stack:
    """Стек на базе списка."""

    def __init__(self):
        self._data = []

    def push(self, item):
        """Добавить элемент на вершину стека."""
        self._data.append(item)

    def pop(self):
        """Удалить и вернуть элемент с вершины стека."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        """Вернуть элемент с вершины без удаления."""
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self):
        """Проверить, пуст ли стек."""
        return len(self._data) == 0

    def __len__(self):
        """Вернуть количество элементов."""
        return len(self._data)

    def __repr__(self):
        """Строковое представление."""
        return f"Stack({self._data})"


class Queue:
    """Реализация очереди на базе deque."""

    def __init__(self) -> None:
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Добавить элемент в конец очереди."""
        self._data.append(item)

    def dequeue(self) -> Any:
        """Удалить и вернуть элемент из начала очереди."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> Optional[Any]:
        """Вернуть элемент из начала без удаления."""
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """Проверить, пуста ли очередь."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Вернуть количество элементов в очереди."""
        return len(self._data)

    def __repr__(self) -> str:
        """Вернуть строковое представление очереди."""
        return f"Queue({list(self._data)})"