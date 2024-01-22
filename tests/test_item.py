"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

import pytest

from config import file_path
from src.item import Item


def test_calculate_total_price():
    item1 = Item("Book", 1000, 2)
    item2 = Item("Book", 1000.5, 2)
    assert item1.calculate_total_price() == 2000
    assert item2.calculate_total_price() == 2001


def test_apply_discount():
    item1 = Item("Book", 500.0, 2)
    item1.pay_rate = 0.9
    item1.apply_discount()
    assert item1.price == 450.0


def test_name():
    item1 = Item('Смартфон', 500.0, 2)
    assert item1.name == 'Смартфон'
    item2 = Item('СуперСмартфон', 500.0, 2)
    assert item2.name == 'СуперСмартфон'


def test_instantiate_from_csv():
    Item.instantiate_from_csv(file_path)
    item1 = Item('Смартфон', 500.0, 2)
    assert isinstance(Item.all, list)
    assert item1.name == "Смартфон"
    assert item1.price == 500
    assert item1.quantity == 2


def test_instantiate_from_csv_not_file():
    with pytest.raises(FileNotFoundError):
        with open('../src/ite.csv', encoding='cp1251') as csvfile:
            csv.DictReader(csvfile)


def test_string_to_number():
    assert Item.string_to_number('7') == 7
    assert Item.string_to_number('8.0') == 8
    assert Item.string_to_number('4.5') == 4


def test_repr():
    item1 = Item('Notebook', 500.0, 2)
    assert repr(item1) == "Item('Notebook', 500.0, 2)"


def test_str():
    item1 = Item('Notebook', 500.0, 2)
    assert str(item1) == 'Notebook'
