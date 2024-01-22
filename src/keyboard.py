from src.item import Item


class MixinLanguage:
    __language = "EN"

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, change_language):
        if change_language in ["EN", "RU"]:
            self.__language = change_language
        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
            return self


class Keyboard(Item, MixinLanguage):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
