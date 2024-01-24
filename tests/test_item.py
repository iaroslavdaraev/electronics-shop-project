"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv
from _operator import add

import pytest

from config import file_path, broken_file_path
from src.item import Item, InstantiateCSVError
from src.phone import Phone


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


def test_name_setter():
    item1 = Item('Смартфон', 500.0, 2)
    item1.name = 'PDA'
    assert item1.name == 'PDA'


def test_instantiate_from_csv():
    Item.instantiate_from_csv(file_path)
    item1 = Item('Смартфон', 500.0, 2)
    assert isinstance(Item.all, list)
    assert item1.name == "Смартфон"
    assert item1.price == 500
    assert item1.quantity == 2


def test_instantiate_from_csv_not_file():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("плохой путь")


def test_instantiate_from_csv_corrupted_file():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(broken_file_path)


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


def test_add():
    item1 = Item('Смартфон', 500.0, 2)
    phone1 = Phone('Nokia', 50000.0, 2, 7)
    assert add(item1.price,phone1.price) == 50500.0
    assert add(item1.quantity,phone1.price) == 50002
    assert add(item1.price,phone1.price) == 50500.0
