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