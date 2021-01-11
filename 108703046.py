import numpy as np
t = np.array([[0.3,0.2,0.5],[0.1,0.3,0.6],[0.5,0.4,0.1]]) #完成定義 t 為上述矩陣
print(t)

t2 = np.dot(t, t)
print(t2)

t5 = np.dot(np.dot(t2,t2),t)
print(t5)

t5error = np.power(t,5)
print(t5error)

s = np.matrix([[0.3,0.2,0.5],[0.1,0.3,0.6],[0.5,0.4,0.1]]) # 使用 np.matrix 來完成定義
print(s)

s2 = np.matmul(s, s)
print(s2)

from numpy.linalg import matrix_power
t10 = matrix_power(t,10) # 完成這一個指令的參數
print(t10)

s10 = matrix_power(s,10)
print(s10)

x = np.matrix([[0.1,0.2,0.7,0,0],[0,0.2,0.1,0.7,0],[0,0,0.1,0.2,0.7],[0.7,0,0,0.2,0.1],[0.2,0.7,0,0,0.1]]) # 完成指令
print(x)

x2 = matrix_power(x,15)
print(x2)

x3 = matrix_power(x,100)
print(x3)

x4 = matrix_power(x,101)
print(x4)
