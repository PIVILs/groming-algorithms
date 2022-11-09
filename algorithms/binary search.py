n = int(input('Колличество элементов: '))
item = int(input('Искомое целое значение: '))

lst = list(range(n))

def binary_search(list, item):
    """Функция бинарного поиска"""
    low = list[0]
    high = len(list) - 1
    x = 0

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        x += 1
        if guess == item:
            return print(mid, 'шагов поиска' f' {x}')
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return print('Нет среди элементов')

binary_search(lst, item)