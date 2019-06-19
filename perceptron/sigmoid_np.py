import numpy as np
import math


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


a = np.array([[-1, -1], [0, 0]])

# res = sigmoid(a)
res = np.vectorize(sigmoid)(a)
print(res)