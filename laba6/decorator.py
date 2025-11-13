# Містить декоратор, який перевіряє роль користувача
def access_required(required_role):
    # Створення декоратора з параметром ролі
    def decorator(func):
        # Обгортка для функції, яку потрібно захистити
        def wrapper(user):
            # Перевірка, чи роль користувача збігається з потрібною
            if user["role"] != required_role:
                # Якщо роль не підходить, викликається помилка
                raise PermissionError("Доступ заборонено!")
            # Якщо роль правильна, виконується основна функція
            return func(user)
        return wrapper
    return decorator
