# Імпорт бібліотек
import requests        # веб-запити
import numpy as np     # масиви та математика
import pandas as pd    # таблиці
import matplotlib.pyplot as plt  # графіки
from PIL import Image  # робота з зображеннями
from bs4 import BeautifulSoup  # HTML парсинг
from dateutil import parser    # робота з датами
import pyfiglet        # ASCII-текст
from tqdm import tqdm   # прогрес-бар
from faker import Faker # фейкові дані

# 1. Requests
try:
    r = requests.get("https://httpbin.org/get")
    print("Requests:", r.status_code)
except Exception as e:
    print("Requests помилка:", e)

# 2. NumPy
try:
    print("NumPy:", np.array([1, 2, 3]) + 5)
except Exception as e:
    print("NumPy помилка:", e)

# 3. Pandas
try:
    print("Pandas:\n", pd.DataFrame({"a":[1,2], "b":[3,4]}))
except Exception as e:
    print("Pandas помилка:", e)

# 4. Pyfiglet
try:
    print(pyfiglet.figlet_format("Lab5"))
except Exception as e:
    print("Pyfiglet помилка:", e)

# 5. Faker
try:
    fake = Faker()
    print("Faker:", fake.name())
except Exception as e:
    print("Faker помилка:", e)

print("Готово")



