list = [15, 2, 47, 33, 8, 56, 11, 90, 5, 28,
             'apple', 'banana', 'cherry', 'grape', 'lemon', 'mango', 'peach', 'plum', 'kiwi', 'pear']
# Створюємо початковий список list, який містить як числа (int), так і рядки (str)
int_elements = [x for x in list if isinstance(x, int)]
# Створюємо список int_elements, в якому залишаємо тільки ті елементи з list, які є цілими числами (int), використовуючи перевірку isinstance яка перевіряє, чи є об'єкт екземпляром класу int
str_elements = [x for x in list if isinstance(x, str)]
# Створюємо список str_elements, в якому залишаємо тільки ті елементи з list, які є рядками (str), за допомогою isinstance яка перевіряє, чи є об'єкт екземпляром певного класу str
int_sorted = sorted(int_elements)
# Сортуємо список цілих чисел int_elements за зростанням і записуємо результат у int_sorted
str_sorted = sorted(str_elements)
# Сортуємо список рядків str_elements в алфавітному порядку і записуємо у str_sorted
combined_sorted = int_sorted + str_sorted
# Об'єднуємо відсортовані списки int_sorted і str_sorted у новий список combined_sorted, де спочатку йдуть числа, потім рядки
# Всі int-елементи, кратні двом
evens = [x for x in int_sorted if x % 2 == 0]
# Створюємо список evens, що містить лише ті цілі числа з int_sorted, які діляться на 2 без остачі (кратні двом)
str_caps = [x.upper() for x in str_elements]
# Створюємо список str_caps, де всі рядки зі str_elements перетворені у верхній регістр за допомогою методу upper()
print('Основний список (list):', list)
# Виводимо початковий список list на екран
print('Відсортований список (sorted, int + str):', combined_sorted)
# Виводимо об'єднаний відсортований список combined_sorted
print('Елементи кратні двом (evens):', evens)
# Виводимо список evens з числами, кратними двом
print('Список str написаний капсом (str_caps):', str_caps)
# Виводимо список рядків у верхньому регістрі str_caps