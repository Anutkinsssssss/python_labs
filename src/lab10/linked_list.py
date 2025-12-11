from typing import Any, Optional, Iterator


class Node:
    """Узел односвязного списка."""

    def __init__(self, value: Any, next_node: Optional['Node'] = None) -> None:
        self.value: Any = value
        self.next: Optional['Node'] = next_node

    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    """Односвязный список."""

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        """Добавить элемент в конец списка."""
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, value: Any) -> None:
        """Добавить элемент в начало списка."""
        new_node = Node(value, self.head)
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """Вставить элемент по индексу."""
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")

        if idx == 0:
            self.prepend(value)
        elif idx == self._size:
            self.append(value)
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next

            new_node = Node(value, current.next)
            current.next = new_node
            self._size += 1

    def remove_at(self, idx: int) -> None:
        """Удалить элемент по индексу."""
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size})")

        if idx == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next

            current.next = current.next.next

            if current.next is None:
                self.tail = current

        self._size -= 1

    def remove(self, value: Any) -> bool:
        """Удалить первое вхождение значения."""
        if self.is_empty():
            return False

        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True

        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next

        if current.next is None:
            return False

        current.next = current.next.next
        if current.next is None:
            self.tail = current

        self._size -= 1
        return True

    def is_empty(self) -> bool:
        """Проверить, пуст ли список."""
        return self.head is None

    def __len__(self) -> int:
        """Вернуть количество элементов."""
        return self._size

    def __iter__(self) -> Iterator[Any]:
        """Итератор по значениям списка."""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __repr__(self) -> str:
        """Вернуть строковое представление списка."""
        items = list(self)
        return f"SinglyLinkedList({items})"

    def __str__(self) -> str:
        """Вернуть красивое представление списка."""
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.value))
            current = current.next
        return " -> ".join(result) + " -> None"