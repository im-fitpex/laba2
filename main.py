import re
import requests
import unittest

# Функция для проверки номера телефона
def validate_phone_number(phone_number):
    # Регулярное выражение для поддержки номеров без разделителей
    pattern = r"^(?:\+7|8)\d{10}$|^(?:\+7|8)\s?\(?\d{3}\)?\s?\d{3}-\d{2}-\d{2}$"
    return bool(re.match(pattern, phone_number))

# Функция для поиска номеров телефонов на веб-странице по URL
def find_phone_numbers_in_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Регулярное выражение для поиска в тексте страницы
        pattern = r"(?:\+7|8)\d{10}$|(?:\+7|8)\s?\(?\d{3}\)?\s?\d{3}-\d{2}-\d{2}"
        return re.findall(pattern, response.text)
    return []

# Функция для поиска номеров телефонов в загруженном файле
def find_phone_numbers_in_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        # Обновленное регулярное выражение для поиска в файле
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
            "+7 123 4567890",    # Без разделителей
            "123 456 7890",      # Без кода страны
            "8 123-456-78-90",    # Неверный формат
            "8 (123) 456-7890"    # Неверный формат
        ]
        for number in invalid_numbers:
            self.assertFalse(validate_phone_number(number))


if __name__ == '__main__':
    # Пример проверки телефона
    print(validate_phone_number("+7 (123) 456-78-90"))  # True
    print(validate_phone_number("81234567890"))  # True
    print(validate_phone_number("+79999999999"))  # True
    print(validate_phone_number("89999999999"))  # True

    # Пример поиска номеров по URL
    url = 'https://example.com'
    phone_numbers = find_phone_numbers_in_url(url)
    print(phone_numbers)

    # Пример поиска номеров в файле
    filename = 'file.txt'
    phone_numbers_in_file = find_phone_numbers_in_file(filename)
    print(phone_numbers_in_file)

    # Запуск unit-тестов
    unittest.main(argv=[''], exit=False)