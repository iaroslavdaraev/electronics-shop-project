"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item1 = Item("Book", 1000, 2)
    item2 = Item("Book", 1000.5, 2)
    assert Item.calculate_total_price(item1) == 2000
    assert Item.calculate_total_price(item2) == 2001


def test_apply_discount():
    pay_rate = 2.0
    item1 = Item("Book", 500, 2)
    assert Item.apply_discount(item1) == None
