# Імпорт декоратора з іншого файлу
from decorator import access_required
# Використання декоратора для функції, доступної лише адміністраторам
@access_required("admin")
def delete_user(user):
    # Повідомлення, якщо користувач має потрібну роль
    print(f"{user['name']} може видаляти користувачів.")
# Створення прикладів користувачів із різними ролями
user1 = {"name": "Лера", "role": "admin"}
user2 = {"name": "Іван", "role": "user"}
# Виклик функції з користувачем, який має роль admin
try:
    delete_user(user1)
except PermissionError as e:
    print(e)
# Виклик функції з користувачем, який не має потрібної ролі
try:
    delete_user(user2)
except PermissionError as e:
    print(e)