import numpy as np
'''
    数组的转置
    transpose方法  或.T
'''

#创建二维数组
a=np.arange(1,25).reshape(8,3)
print(a)
print('transpose函数进行数组转置a[i][j]--a[j][i]')
b=a.transpose()
print(b,b.shape)

#也可以通过.T
print(a.T,a.shape)

#numpy中的transpose()
c=np.transpose(a)
print(c,c.shape)

#多维数组的转置
print('多维数组的转置')
print('-'*50)
a=a.reshape(2,3,4)
print(a,a.shape)

print('对于三维a[i][j][k]进行转置，默认是将i和k进行交换')
b=np.transpose(a)
print(b,b.shape)

#(2,3,4) ->(3,4,2)
#默认是(0,1,2)数字代表下标
print('-'*50)
c=np.transpose(a,(1,2,0))
print(c,c.shape)
