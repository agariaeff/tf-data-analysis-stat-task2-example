import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 540157708 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    alpha = 1 - p
    t_alpha_2 = expon.ppf(1 - alpha / 2)
    loc = np.mean(x)
    s2 = np.var(x, ddof=1)
    se = np.sqrt(s2 / n)

    lower = loc - se * t_alpha_2 / (2 * loc)
    upper = loc + se * t_alpha_2 / (2 * loc)

    return (lower, upper)
