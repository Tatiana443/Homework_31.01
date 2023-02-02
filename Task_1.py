# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример: 5 -> 1 0 1 1 0 --> 2
coins = int(input('coins: '))
head_count = 0
tail_count = 0
for i in range(coins):
    side = int(input('side: '))
    if side == 1:
        head_count += 1
    elif side == 0:
        tail_count += 1
print(head_count if (head_count < tail_count) else tail_count)
