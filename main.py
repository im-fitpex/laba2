import re
import requests
import unittest

# Функция для проверки номера телефона
def validate_phone_number(phone_number):
    # Регулярное выражение для поддержки номеров без разделителей
    pattern = r"^(?:\+7|8)\d{10}$|^(?:\+7|8)\s?\(?\d{3}\)?\s?\d{3}-\d{2}-\d{2}$"
    return bool(re.match(pattern, phone_number))

# Функция для поиска номеров телефонов в загруженном файле
def find_phone_numbers_in_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        # Регулярное выражение для поиска в файле
        pattern = r"(?:\+7|8)\d{10}|(?:\+7|8)\s?\(?\d{3}\)?\s?\d{3}-\d{2}-\d{2}"
        return re.findall(pattern, content)

# Unit-тесты для проверки корректности регулярного выражения
class TestPhoneNumberValidation(unittest.TestCase):
    def test_valid_phone_numbers(self):
        valid_numbers = [
            "+7 (123) 456-78-90",
            "8 (123) 456-78-90",
            "+7 123 456-78-90",
            "8 123 456-78-90",
            "+79999999999",
            "89999999999"
        ]
        for number in valid_numbers:
            self.assertTrue(validate_phone_number(number))

    def test_invalid_phone_numbers(self):
        invalid_numbers = [
            "+7 123 4567890",  # Без разделителей
            "123 456 7890",  # Без кода страны
            "8 123-456-78-90",  # Неверный формат
            "8 (123) 456-7890"  # Неверный формат
        ]
        for number in invalid_numbers:
            self.assertFalse(validate_phone_number(number))

if __name__ == '__main__':
    print("Выберите опцию:")
    print("1. Ввести номера вручную")
    print("2. Проверить номера из файла")
    print("3. Провести UNIT тесты")
    choice = input("Введите ваш выбор (1 или 2): ")
    if choice == '1':
        print("Введите номера телефонов для проверки. Оставьте строку пустой, чтобы завершить ввод.")
        while True:
            phone_input = input("Введите номер: ")
            if not phone_input.strip():  # Проверка на пустую строку
                break
            if validate_phone_number(phone_input):
                print(f"Номер {phone_input} валиден.")
            else:
                print(f"Номер {phone_input} невалиден.")
    elif choice == '2':
        filename = input("Введите имя файла: ")
        try:
            phone_numbers_in_file = find_phone_numbers_in_file(filename)
            if phone_numbers_in_file:
                print("Найденные номера телефонов:")
                for number in phone_numbers_in_file:
                    print(number)
            else:
                print("В файле не найдено номеров телефонов.")
        except FileNotFoundError:
            print("Файл не найден. Проверьте путь и попробуйте снова.")
    elif choice == '3':
        unittest.main(argv=[''], exit=False)
    else:
        print("Некорректный выбор. Попробуйте снова.")
