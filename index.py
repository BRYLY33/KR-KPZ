import re


userString = input(
    "Введите что-то в camelCase, функция вернет строку в snake_case -->: ")
userString = re.sub(r'(?<!^)(?=[A-Z])', '_', userString).lower()
print(userString)

pattern = re.compile(r'(?<!^)(?=[A-Z])')
userString = pattern.sub('_', userString).lower()


def to_snake_case(userString):
    userString = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', userString)
    userString = re.sub('__([A-Z])', r'_\1', userString)
    userString = re.sub('([a-z0-9])([A-Z])', r'\1_\2', userString)
    return userString.lower()
