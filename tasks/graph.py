from typing import TypeVar, Generic
from collections import deque

__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root

    def dfs_rec(self) -> list[Node]:
        visited: set[Node] = set()
        result: list[Node] = []

        def rec(node: Node) -> None:
            if node in visited:
                return
            result.append(node)
            visited.add(node)
            for adjacent_node in node.outbound:
                rec(adjacent_node)

        rec(self._root)
        return result

    def dfs(self) -> list[Node]:
        visited: set[Node] = set()
        result: list[Node] = []

        stack: list[Node] = [self._root]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            result.append(node)
            visited.add(node)
            stack.extend(reversed(node.outbound))

        return result

    def bfs(self) -> list[Node]:
        visited: set[Node] = set()
        result: list[Node] = []

        queue: deque[Node] = deque([self._root])
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            queue.extend(node.outbound)
            result.append(node)

        return result
