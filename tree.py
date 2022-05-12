import json
from re import Match
from typing import Optional, AnyStr
import re

from custom_exceptions import NodeMissingError
from custom_exceptions.not_exists_prefix_error import NotExistsPrefixError


class Tree:
    def __init__(self, root: Optional[str] = None) -> None:
        self._root: Optional["str"] = root
        self._left: Optional["Tree"] = None
        self._right: Optional["Tree"] = None

    def append(self, root, child_value) -> None:
        if root is None:
            self._root = child_value
            return
        if self._left is None:
            self._left = self._fill_empty_child(root, child_value)
        elif child_value.startswith(self._left._root):
            self._left.append(root, child_value)
        elif self._right is None:
            self._right = self._fill_empty_child(root, child_value)
        elif child_value.startswith(self._right._root):
            self._right.append(root, child_value)
        else:
            raise NodeMissingError("Пропущен узел: \"{root}\"")

    def _fill_empty_child(self, root, child_value) -> "Tree":
        if root != self._root:
            raise NodeMissingError(f"Пропущен узел: \"{root}\"")
        return Tree(child_value)

    def dict(self) -> dict:
        result: dict = {
            self._root: {}
        }
        if self._left:
            result[self._root].update(self._left.dict())
        if self._right:
            result[self._root].update(self._right.dict())
        return result

    def json(self, indent: int = 4) -> str:
        return json.dumps(self.dict(), indent=indent)


class Saplings:
    def __init__(self) -> None:
        self._saplings: dict[str, Tree] = {}

    @staticmethod
    def _get_prefix(name: str) -> str:
        prefix: Optional[Match[AnyStr]] = re.search(r'^[a-zA-Z]+', name)
        if prefix is None:
            raise NotExistsPrefixError("Префикс отсутствует")
        return prefix.group()

    def add_tree(self, root: Optional[str], child: str) -> None:
        sapling_name: str = self._get_prefix(child)
        if root is None:
            tree: Tree = Tree(child)
            self._saplings[sapling_name] = tree
        elif self._saplings.get(sapling_name) is None:
            raise NodeMissingError("Пропущен основной узел")
        else:
            self._saplings[sapling_name].append(root, child)

    def get_first(self) -> Tree:
        return next(iter(self._saplings.values()))

    def dict(self) -> dict:
        result: dict = {}
        for tree in self._saplings.values():
            result.update(tree.dict())
        return result

    def json(self, indent: int = 4) -> str:
        return json.dumps(self.dict(), indent=indent)


def create_tree_from_list(nodes: list) -> dict:
    saplings: Saplings = Saplings()
    for node in nodes:
        saplings.add_tree(*node)
    return saplings.dict()


if __name__ == '__main__':
    source: list = [
        (None, 'a'),
        (None, 'b'),
        (None, 'c'),
        ('a', 'a1'),
        ('a', 'a2'),
        ('a2', 'a21'),
        ('a2', 'a22'),
        ('b', 'b1'),
        ('b1', 'b11'),
        ('b11', 'b111'),
        ('b', 'b2'),
        ('c', 'c1')
    ]

    expected: dict = {
        'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
        'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
        'c': {'c1': {}},
    }

    print(create_tree_from_list(source) == expected)
