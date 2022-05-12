import unittest

from tree import create_tree_from_list


class TestStringMethods(unittest.TestCase):

    def test_1_create_three_from_list(self) -> None:
        nodes: list = [
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

        self.assertEqual(create_tree_from_list(nodes), expected)


if __name__ == '__main__':
    unittest.main()
