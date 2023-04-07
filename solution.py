import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 975846018 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    
    alpha = 0.01  # уровень значимости
    statistic, pvalue = ks_2samp(x, y)
    return pvalue < alpha
