import numpy as np

'''
    数组的水平拼接与垂直拼接,可以通过hstack（水平方向）,vstack（垂直方向）进行拼接
    concatenate:连接沿指定轴连接相同形状的两个或多个数组
    numpy.concatenate((a1,a2,...),axis)
        参数说明：a1,a2,...:相同类型的数组
        axis:沿着它连接数组的轴，默认为0（垂直方向,相当于vstack）
    
'''

#创建两个数组
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[11,12,13],[14,15,16]])
print(a)
print('-'*50)
print(b)
#使用hstack进行水平拼接
print('使用hstack进行水平拼接')
r=np.hstack([a,b])
r=np.hstack((a,b))
print(r)

#使用vstack进行垂直方向的拼接
print('-'*50)
print('使用vstack进行垂直方向的拼接')
r=np.vstack([a,b])
print(r)

#concatenate的使用
print('-'*50)
print('concatenate的使用,默认情况axis=0，相当于vstack')
r1=np.concatenate((a,b),axis=0)
r2=np.concatenate((a,b))
print(r1)
print("-------")
print(r2)

# 二维数组有两个轴,axis=0,axis=1(水平)
print('axis=1，水平方向拼接，相当于hstack')
r3=np.concatenate((a,b),axis=1)
print(r3)

# 三维数组有三个轴，axis=0,axis=1,axis=2
print('-'*50)
print('三维数组有三个轴')
a = np.arange(1,13).reshape((1,2,6))
print(a.shape)
print(a)
b = np.arange(101,113).reshape((1,2,6))
print(b.shape)
print(b)
print('三维 axis=0')
r1=np.concatenate((a,b),axis=0)
print(r1,r1.shape)

print('三维 axis=1')
r2=np.concatenate((a,b),axis=1)
print(r2,r2.shape)

print('三维 axis=2')
r3=np.concatenate((a,b),axis=2)
print(r3,r3.shape)