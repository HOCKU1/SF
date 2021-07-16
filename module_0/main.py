import numpy as np


def score_game(game_core):
    # Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game_core_v3(number):
    np.random.randint = list(range(1, 101))  # Загаданное число
    low = 1  # Минимальное значени
    high = 100  # Максимальное значение
    index = 0
    count = 1  # Колличество попыток
    while (low <= high) and (index == 0):
        count += 1
        mid = (low + high) // 2
        if np.random.randint[mid] == number:
            index = mid
        else:
            if number < np.random.randint[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return count


score_game(game_core_v3)
