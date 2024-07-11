# Модули и пакеты
from true_math import divide as div_true
from fake_math import divide as div_fake

result1 = div_fake(69, 3)
result2 = div_fake(3, 0)
result3 = div_true(49, 7)
result4 = div_true(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)

# Вывод на консоль:
# 23.0
# Ошибка
# 7.0
# inf