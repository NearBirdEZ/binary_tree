import unittest

from custom_exceptions import NodeMissingError
from tree import Tree


class TestTree(unittest.TestCase):
    @staticmethod
    def _generate_tree(input_tree: list[tuple]) -> dict:
        tree: Tree = Tree()
        for row in input_tree:
            tree.append(*row)
        return tree.dict()

    def test_1_generate_tree(self):
        input_tree: list[tuple] = [
            (None, 'a'),
            ('a', 'a1'),
            ('a', 'a2'),
            ('a2', 'a21'),
            ('a2', 'a22')
        ]
        answer: dict = {
            "a": {
                "a1": {},
                "a2": {
                    "a21": {},
                    "a22": {}
                }
            }
        }
        tree: dict = self._generate_tree(input_tree)
        self.assertEqual(tree, answer)

    def test_2_generate_tree(self):
        input_tree: list[tuple] = [
            (None, 'b'),
            ('b', 'b1'),
            ('b1', 'b11'),
            ('b11', 'b111'),
            ('b', 'b2'),
        ]
        answer: dict = {
            "b": {
                "b1": {
                    "b11": {
                        "b111": {}
                    }
                },
                "b2": {}
            }
        }
        tree: dict = self._generate_tree(input_tree)
        self.assertEqual(tree, answer)

    def test_3_generate_tree(self):
        input_tree: list[tuple] = [
            (None, 'c'),
            ('c', 'c1')
        ]
        answer: dict = {
            "c": {
                "c1": {}
            }
        }

        tree: dict = self._generate_tree(input_tree)
        self.assertEqual(tree, answer)

    def test_4_generate_failed_tree(self):
        input_tree: list[tuple] = [
            (None, 'c'),
            ('a', 'a1')
        ]
        tree: Tree = Tree()
        with self.assertRaises(NodeMissingError):
            for row in input_tree:
                tree.append(*row)

    def test_5_generate_failed_tree(self):
        input_tree: list[tuple] = [
            (None, 'c'),
            ('c1', 'c2')
        ]
        tree: Tree = Tree()
        with self.assertRaises(NodeMissingError):
            for row in input_tree:
                tree.append(*row)


if __name__ == '__main__':
    unittest.main()
