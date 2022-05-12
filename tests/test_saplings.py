import unittest

from custom_exceptions import NodeMissingError
from custom_exceptions import NotExistsPrefixError
from tree import Saplings


class TestSaplings(unittest.TestCase):

    def test_1_generate_sapling(self) -> None:
        saplings: Saplings = Saplings()
        nodes: list[tuple] = [
            (None, 'a'),
            (None, 'b'),
            (None, 'c'),
            (None, 'd'),
            ('a', 'a1'),
            ('a', 'a2'),
            ('a2', 'a21'),
            ('a2', 'a22'),
            ('b', 'b1'),
            ('b1', 'b11'),
            ('b11', 'b111'),
            ('b', 'b2'),
            ('c', 'c1'),
        ]
        answer: dict = {
            'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
            'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
            'c': {'c1': {}},
            'd': {}
        }
        for node in nodes:
            saplings.add_tree(*node)
        self.assertEqual(saplings.dict(), answer)

    def test_2_generate_sapling(self) -> None:
        saplings: Saplings = Saplings()
        nodes: list[tuple] = [
            (None, 'b'),
            (None, 'c'),
            ('b', 'b1'),
            ('b1', 'b11'),
            ('b11', 'b111'),
            ('b', 'b2'),
            ('c', 'c1'),
        ]
        answer: dict = {
            'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
            'c': {'c1': {}},
        }
        for node in nodes:
            saplings.add_tree(*node)
        self.assertEqual(saplings.dict(), answer)

    def test_3_generate_sapling(self) -> None:
        saplings: Saplings = Saplings()
        nodes: list[tuple] = [
            (None, 'a'),
            (None, 'b'),
            (None, 'c'),
        ]
        answer: dict = {
            'a': {},
            'b': {},
            'c': {}
        }
        for row in nodes:
            saplings.add_tree(*row)
        self.assertEqual(saplings.dict(), answer)

    def test_4_generate_failed_sapling(self) -> None:
        saplings: Saplings = Saplings()
        nodes: list[tuple] = [
            (None, 'b'),
            (None, 'c'),
            ('b', 'b1'),
            ('b11', 'b111'),
            ('b', 'b2'),
            ('c', 'c1'),
        ]
        with self.assertRaises(NodeMissingError):
            for node in nodes:
                saplings.add_tree(*node)

    def test_5_generate_failed_sapling(self) -> None:
        saplings: Saplings = Saplings()
        nodes: list[tuple] = [
            (None, 'c'),
            ('a', 'a1')
        ]
        with self.assertRaises(NodeMissingError):
            for node in nodes:
                saplings.add_tree(*node)

    def test_6_get_prefix(self) -> None:
        saplings: Saplings = Saplings()
        nodes: list[tuple] = [
            (None, 'c'),
            (None, 'ab'),
            (None, 'cd'),
            (None, 'imtree')
        ]
        answer: tuple = (
            'c',
            'ab',
            'cd',
            'imtree',
        )
        for node in nodes:
            saplings.add_tree(*node)
        self.assertEqual(tuple(saplings.dict().keys()), answer)

    def test_6_get_failed_prefix(self) -> None:
        saplings: Saplings = Saplings()
        nodes: list[tuple] = [
            (None, 'c'),
            (None, 'ab'),
            (None, '1cd'),
            (None, 'imtree')
        ]
        with self.assertRaises(NotExistsPrefixError):
            for node in nodes:
                saplings.add_tree(*node)


if __name__ == '__main__':
    unittest.main()
