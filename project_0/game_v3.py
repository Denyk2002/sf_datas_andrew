import numpy as np

def game_core_v3(number:int=1) -> int:
    """Игра угадываем число
    Функция принимает загаданное число и возвращает число попыток
    Используем бинарный поиск
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    # Устанавливаем концы отрезка
    left, right = 1, 100
    predict = 0  
    while predict != number:
        count += 1
        # Вычислить середину
        mid = left + (right-left)//2
        if number > mid: 
            left = mid+1
            predict = left  
        else: 
            right = mid-1
            predict = right   
                          
    return count 


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) 
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
     
    return score     
  
if __name__ == " __main__ ":
    score_game(game_core_v3)