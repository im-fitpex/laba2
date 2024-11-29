import re
import requests
import unittest

# Функция для проверки номера телефона
def validate_phone_number(phone_number):
    # Обновленное регулярное выражение для поддержки номеров без разделителей
    pattern = r"^(?:\+7|8)\d{10}$|^(?:\+7|8)\s?\(?\d{3}\)?\s?\d{3}-\d{2}-\d{2}$"
    return bool(re.match(pattern, phone_number))
