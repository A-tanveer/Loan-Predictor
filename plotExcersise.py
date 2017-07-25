# import numpy as np
# from matplotlib.pyplot import step, xlim, ylim, show
# x = np.arange(0, 7)
# y = np.array([0, 1, 0, 1, 1, 0, 1])
# xlim(0, 7)
# ylim(-0.5, 1.5)
# step(x, y)
# show()
#
# import re
# print(re.sub("[^0-9.]", "", ">125.45$"))

x = ['21,0,45,7,45.21', '21,0,45,7,45.21', '21,0,45,7,45.21']
X = []
for i in x:
    X.append(list(map(float, i.split(','))))
# X = list(map(float, X))
print(X)
