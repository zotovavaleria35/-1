import random                      # Для випадкових виборів
import string                      # Щоб взяти англійські букви


def create_random_file(filename, lines_count=101, words_per_line=10):
    """Створює файл з випадковими словами, розділеними пробілами"""
    with open(filename, "w", encoding="utf-8") as f:  # Відкриваємо файл для запису
        for _ in range(lines_count):                 # Для кожного рядка
            words = []                               # Створюємо порожній список слів
            for _ in range(words_per_line):          # Створюємо кілька слів на рядок
                word_length = random.randint(3, 8)   # Довжина слова від 3 до 8 букв
                word = ''.join(random.choice(string.ascii_lowercase)  # Створюємо слово з випадкових букв
                               for _ in range(word_length))
                words.append(word)                  # Додаємо слово в список
            line = ' '.join(words)                  # З'єднуємо слова через пробіл
            f.write(line + "\n")                    # Записуємо рядок у файл і додаємо новий рядок


def count_pairs(filename, pairs_list_per_line):
    """Генератор, який рахує пари букв у кожному рядку"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:  # Відкриваємо файл для читання
            for line_index, line in enumerate(f):        # Беремо рядок і його номер
                pairs = pairs_list_per_line[line_index]  # Беремо 3 пари для цього рядка
                pair_counts = {p: 0 for p in pairs}      # Створюємо словник для підрахунку

                words = line.strip().split()            # Розбиваємо рядок на слова за пробілами

                for word in words:                      # Перебираємо слова
                    word = word.lower()                 # Перетворюємо в нижній регістр
                    for i in range(len(word) - 1):     # Беремо кожні дві букви підряд
                        pair = word[i:i+2]             # Виділяємо пару букв
                        if pair in pair_counts:        # Якщо ця пара серед потрібних
                            pair_counts[pair] += 1     # Додаємо +1 до рахунку

                yield pair_counts                         # Повертаємо словник для цього рядка

    except Exception as e:                                 # Якщо виникла помилка
        print(f"Помилка: {e}")                             # Виводимо повідомлення
        return                                             # Завершуємо функцію


def main():
    FILE = "random_text.txt"  # Назва файлу для збереження

    create_random_file(FILE, lines_count=101, words_per_line=12)  # Створюємо файл з 12 словами на рядок

    all_pairs = []                                         # Список для збереження 3 пар на кожен рядок
    letters = string.ascii_lowercase                       # Англійські букви a-z

    for _ in range(101):                                   # Для кожного рядка
        three_pairs = set()                                 # Множина для унікальних пар
        while len(three_pairs) < 3:                         # Поки не буде 3 різні пари
            pair = random.choice(letters) + random.choice(letters)  # Створюємо випадкову пару букв
            three_pairs.add(pair)                            # Додаємо пару до множини
        all_pairs.append(list(three_pairs))                 # Додаємо 3 пари у список

    result = count_pairs(FILE, all_pairs)                  # Викликаємо генератор для підрахунку пар

    for i, res in enumerate(result, start=1):              # Для кожного рядка
        print(f"Рядок №{i}, пари {all_pairs[i-1]}: {res}")  # Виводимо номер рядка, пари та їх кількість


if __name__ == "__main__":
    main()                                                 # Запускаємо програму