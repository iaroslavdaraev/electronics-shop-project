from src.keyboard import Keyboard


def test_keyboard_init():
    kb = Keyboard('Defender M900', 5700, 15)
    assert kb.name == 'Defender M900'
    assert kb.price == 5700
    assert kb.quantity == 15
    assert kb.language == 'EN'


def test_language():
    kb = Keyboard('Defender M900', 5700, 15)
    kb.change_lang()
    assert str(kb.language) == 'RU'


def test_change_lang():
    kb = Keyboard('Defender M900', 5700, 15)
    assert str(kb.language) == 'EN'
    assert str(kb.language) != 'CH'
