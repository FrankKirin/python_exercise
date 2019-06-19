import numpy as np

xAll = np.array(([2, 9], [1, 5], [3, 6], [5, 10]), dtype=float)
y = np.array([[92], [86], [89]], dtype=float)


xAll = xAll / np.amax(xAll, axis=0)
y = y / 100

X = np.split(xAll, [3])[0]
xPredicted = np.split(xAll, [3])[1]