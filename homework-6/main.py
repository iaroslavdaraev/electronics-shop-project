from config import broken_file_path
from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv("плохой путь")
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(broken_file_path)
    # InstantiateCSVError: Файл item.csv поврежден
