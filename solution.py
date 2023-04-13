import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 975846018 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # применяем тест Колмогорова-Смирнова к выборкам x и y
    test_result = ks_2samp(x, y)

    # сравниваем p-value с уровнем значимости
    return test_result.pvalue < 0.04
