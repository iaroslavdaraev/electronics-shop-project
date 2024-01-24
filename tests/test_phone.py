import pytest

from src.phone import Phone


def test_repr():
    phone1 = Phone('Nokia', 50000.0, 2, 7)
    assert repr(phone1) == "Phone('Nokia', 50000.0, 2, 7)"

def test_str():
    phone1 = Phone('Nokia', 50000.0, 2, 7)
    assert str(phone1) == 'Nokia'

def test_number_of_sim():
    phone1 = Phone('Nokia', 50000.0, 2, 7)
    assert phone1.number_of_sim == 7


def test_add():
    phone1 = Phone('Nokia', 50000.0, 2, 7)
    with pytest.raises(ValueError) as e:
        phone1.number_of_sim = 0
    assert str(e.value) == 'Cимок должно быть больше 0 и целым числом.'
