results = {}
while True:
    name = input("Введіть ім'я: ")
    if name == "stop":
        break
    grade = int(input("Введіть оцінку: "))
    results[name] = grade
print("Студенти:")
for n in results:
    print(n, results[n])
print("Середній бал:", round(sum(results.values()) / len(results), 2))
exelent = [n for n in results if 10 <= results[n] <= 12]
good = [n for n in results if 7 <= results[n] <= 9]
weak = [n for n in results if 4 <= results[n] <= 6]
fail = [n for n in results if 1 <= results[n] <= 3]
print("Відмінники:", len(exelent), "→", ', '.join(exelent))
print("Хорошисти:", len(good), "→", ', '.join(good))
print("Відстаючі:", len(weak), "→", ', '.join(weak))
print("Не здали:", len(fail), "→", ', '.join(fail))