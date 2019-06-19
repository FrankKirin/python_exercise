"""
    Softmax function
"""

import math
import numpy as np


def softmax(y_pred, type='normal'):
    """
    Params:
    -------
        y_pred: np.array, list, tuple
        type: str, 'normal' or 'log'
        normal return softmax value, log return los_softmax

    Return:    
    -------
        the probability of every y_pred
    """
    prob = []
    total = 0
    for item in y_pred:
        total += math.exp(item)
    for item in y_pred:
        prob.append(math.exp(item) / total)

    return prob


if __name__ == '__main__':
    res = softmax([2, 1, 0.1])
    print(res)
    res = softmax(np.array([1, 2, 3, 4, 5]))
    print(res)
