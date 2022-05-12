# Тестовое задание перед собеседованием на Python

**Требования:**
Написать функцию, строящую дерево по списку пар id (id родителя, id потомка),
где None - id корневого узла.
Пример работы:
```
source = [
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
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

assert to_tree(source) == expected
```
Зависимости отсутствуют <br><br>
Выполнить скрипт:

```
cd ./tree
python tree.py
```

Дополнительное тестирование
```
cd ./tree
python -m unittest ./tests/test_common.py -v
python -m unittest ./tests/test_saplings.py -v
python -m unittest ./tests/test_tree.py -v
```


