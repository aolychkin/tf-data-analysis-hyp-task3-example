import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 1068310526 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.01
    p_value = ttest_ind(x, y, alternative="greater").pvalue
    return p_value < alpha
