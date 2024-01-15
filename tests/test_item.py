"""Здесь надо написать тесты с использованием pytest для модуля item."""
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

# def test_instantiate_from_csv():
#     item_instances = Item.instantiate_from_csv(file_path='src/items.csv')
#     assert isinstance(item_instances, list)

def test_string_to_number():
    assert Item.string_to_number('7') == 7
    assert Item.string_to_number('8.0') == 8
    assert Item.string_to_number('4.5') == 4
