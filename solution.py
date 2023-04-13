import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp


chat_id = 457863109 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.07
    statistic, critical_values, pvalue = anderson_ksamp([x, y])
    return pvalue < alpha # Ваш ответ, True или False
