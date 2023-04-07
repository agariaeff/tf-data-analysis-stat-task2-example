import pandas as pd
import numpy as np

import scipy.stats


chat_id = 540157708 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    time = 38 
    alpha = 1 - p
    semians = 0
    for i in range(len(x)):
      semians += x[i] 
    semians /= len(x) 
    left = semians + scipy.stats.gamma.ppf((alpha)/2, len(x))/len(x) 
    right = semians + scipy.stats.gamma.ppf(1-alpha/2, len(x))/len(x)
    left -= 1/2
    right -= 1/2
    left /= (time**2)
    right /= (time**2)
    left *= 2
    right *= 2

    return left, \
           right
