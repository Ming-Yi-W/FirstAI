import numpy as np

'''
    处理数组的一项重要工作就是改变数组的维度，包含提高数组的维度和降低维度的数组，还包括
    数组的转置。Numpy提供的大量API可以轻松地完成这些数组的操作。例如：通过reshape方法
    可以讲一维数组变成二维，三维或者多维数组。通过ravel方法或flatten方法可以将多维数组变为
    一维数组。改变数组的维度还可以直接设置Numpy数组的shape属性（元组类型），通过resize方法也可以
    改变数组的维度。

'''
print('通过reshape将一维数组修改为二、三维')
#通过reshape将一维数组修改为二、三维
#创建一维数组
a = np.arange(1,25)
#修改为二维(2,12) (4,6) (3,8)
b = a.reshape((4,6))
print(b)
#将一维修改为三维(2,3,4)
c=a.reshape((2,3,4))
print(c)
#也可以通过np.reshape()进行修改
print('通过np.reshape()进行修改')
b=np.reshape(a,(3,8))
print(b)

print('-'*50)
print('将多维数组修改为一维数组')
#c是一个三维数组
# a=c.reshape(24)
#不管你是多少维，统一转换为一维数组
a=c.reshape(-1)
print(a)

print('-'*50)
print('通过ravel,flatten将多维数组修改为一维数组')
#ravel
a=c.ravel()
print(a)
#flatten
a=c.flatten()
print(a)

