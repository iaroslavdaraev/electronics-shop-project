import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    # file_path

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        all_price = self.price * self.quantity
        return all_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, file_path):

        cls.all.clear()
        try:
            with open(file_path, 'r', newline='', encoding="windows-1251") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise InstantiateCSVError("Файл item.csv поврежден.")
                    name = row['name']
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(value: str) -> int:
        return int(float(value))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только экземпляры Item и Phone')
        return self.quantity + other.quantity


class InstantiateCSVError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.message}'
