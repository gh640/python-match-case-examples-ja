"""Python 3.10 で導入された match case 構文でさまざまなパターンを試す"""
import pytest
from dataclasses import dataclass
from enum import Enum


def test_literal_pattern():
    """リテラルパターン"""
    number = 10
    match number:
        case 0:
            assert False
        # 値が一致するものがマッチ
        case 10:
            assert True
        case _:
            assert False


def test_literal_with_or_pattern():
    """or `|` パターン"""
    status = 500
    match status:
        case 200:
            assert False
        # いずれかが一致するものがマッチ
        case 500 | 501 | 502 | 503:
            assert True
        case _:
            assert False


def test_capture_pattern():
    """キャプチャパターン"""
    value = 3.14
    match value:
        case 3:
            assert False
        case 3.1415:
            assert False
        # キャプチャパターンは必ず最後に置く必要がある（でないと SyntaxError ）
        case x:
            assert True
            assert 'x' in locals()
            assert x == 3.14


def test_wildcard_pattern():
    """ワイルドカード `_` パターン"""
    message = 'こんにちは'
    match message:
        case 'おはよう':
            assert False
        # ワイルドカードパターンは必ず最後に置く必要がある（でないと SyntaxError ）
        case _:
            assert True
            # `_` に代入されるわけではない（キャプチャパターンとは異なる点）
            assert '_' not in locals()


def test_value_pattern_1_attrs():
    """バリューパターン 1"""
    class Color:
        RED = 'red'
        YELLOW = 'yellow'
        GREEN = 'green'

    color = 'green'
    match color:
        case Color.RED:
            assert False
        case Color.YELLOW:
            assert False
        # `.` を含むものは単純に値の一致でマッチする
        case Color.GREEN:
            assert True
        case _:
            assert False


def test_value_pattern_2_enum():
    """バリューパターン 2"""
    class Color(Enum):
        RED = 'red'
        YELLOW = 'yellow'
        GREEN = 'green'

    color = Color.GREEN
    match color:
        case Color.RED:
            assert False
        case Color.YELLOW:
            assert False
        case Color.GREEN:
            assert True
        case _:
            assert False


def test_group_pattern():
    """グループパターン"""
    message = 'Nice'
    match message:
        case ('Excellent'):
            assert False
        case ('Nice'):
            assert True
        case _:
            assert False


def test_sequence_pattern_1_list_like_syntax():
    """シーケンスパターン 1"""
    item = ['チョコ', 1, True]
    match item:
        case ['バニラ', 1, True]:
            assert False
        case ['チョコ', count, topping]:
            assert True
            assert count == 1
            assert topping is True


def test_sequence_pattern_2_tuple_like_syntax():
    """シーケンスパターン 2"""
    values = [1, 'Q', 3]
    match values:
        # `(x, y)` と `[x, y]` は同等の扱いになる
        case (1, 'Q', 3):
            assert True
        case _:
            assert False


def test_mapping_pattern():
    adict = {
        'タコ': 'たこ焼き',
        'イカ': 'いか焼き',
    }
    match adict:
        case {'タコ': 'Octopus', 'イカ': 'いか焼き'}:
            assert False
        # 複数行に分けることもできる
        case {
            'タコ': x, 
            'イカ': y,
        }:
            assert True
            assert x == 'たこ焼き'
            assert y == 'いか焼き'
        case _:
            assert False


def test_if_guard():
    """`if` ガード"""
    values = (10, 15)
    match values:
        case x, y if x == y:
            assert False
        case x, y if x > y:
            assert False
        # 10 < 15 なのでここに合致する
        case x, y if x < y:
            assert True
        case _:
            assert False


class Product:
    sku: str
    name: str

    def __init__(self, stock_keeping_unit: str, namae: str):
        """アトリビュート名と引数名を意図的に変えている"""
        self.sku = stock_keeping_unit
        self.name = namae


def test_class_pattern_1_positional_args():
    product = Product('tako', 'たこ焼き')
    match product:
        # `name` が異なる
        case Product(sku='tako', name='タコヤキ'):
            assert False
        # `sku` が異なる
        case Product(sku='otako', name='たこ焼き'):
            assert False
        # `sku` `name` ともに一致
        case Product(sku='tako', name='たこ焼き'):
            assert True
        case _:
            assert False


class Point:
    __match_args__ = ("x", "y")
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y


def test_class_pattern_2_match_args():
    point = Point(3, 5)
    match point:
        case Point(3, 10):
            assert False
        case Point(4, 5):
            assert False
        case Point(3, 5):
            assert True
        case _:
            assert False


def test_class_pattern_3_with_if_guard():
    point = Point(3, 5)
    match point:
        case Point(x, y) if x > y:
            assert False
        case Point(x, y) if x < y:
            assert True
        case _:
            assert False


def test_as_pattern():
    """`as` パターン"""
    points = [Point(3, 5), Point(8, 10)]
    match points:
        case (Point(x1, y1) as p1, Point(x2, y2) as p2):
            assert True 
            assert p1.x == 3
            assert p1.y == 5
            assert p2.x == 8
            assert p2.y == 10
        case _:
            assert False
