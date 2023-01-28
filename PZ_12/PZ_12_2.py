# Из  заданной строки отобразить только символы пунктуации. Использовать
# библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

from string import punctuation

a = '--msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"'
b = (i for i in a if i in punctuation)  # Создаем генератор, который возвращает все знаки пунктуации из строки a
print(*b)  # Выводим все знаки пунктуации из строки a
