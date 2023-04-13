import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 1068310526 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    result = ttest_ind(x, y)
    alpha = 0.01
    return result[1] < alpha
