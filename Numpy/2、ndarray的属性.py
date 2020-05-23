import numpy as np

#ndarray的属性
'''
ndarray.ndim  秩，即轴的数量或维度数量
ndarray.shape   数组的维度，对于矩阵，n行m列
ndarray.size    数组元素的个数，相当于.shape中n*m的值
ndarray.dtype   ndarray对象的元素信息
ndarray.itemsize    ndarray对象中每个元素的大小，以字节为单位
ndarray.flags       ndarray对象的内存信息
ndarray.real        ndarray元素的实部
ndarray.imag        ndarray元素的虚部
ndarray.data        包含实际数组元素的缓冲区
'''

#创建一维数组
a=np.array([1,2,3,4])
print(a)
print('-'*50)
# b=np.arange(4,10)
#创建二维数组
b=np.random.randint(4,10,size=(2,3))
print(b)
print('-'*50)
#创建三维数组
c=np.random.randn(2,3,4)
print(c)
print('-'*50)

#ndmin属性
print('ndmin:',a.ndim,b.ndim,c.ndim)
#shape属性
print('shape',a.shape,b.shape,c.shape)
#dtype属性
print('dtype',a.dtype,b.dtype,c.dtype)
#size属性
print('size',a.size,b.size,c.size)
#itemsize每个元素所占的字节
print('itemsize',a.itemsize,b.itemsize,c.itemsize)

print('-'*50)
print("其他方式创建数组")
#zeros用0来填充
a = np.zeros(5)
print(a)
#和上面的方式等价
b = np.zeros((5,),dtype=int)
print(b)
#创建二维数组
c=np.zeros((3,4))
print(c)

#ones用1来填充,用法和zeros相同
#一维
a=np.ones(5)
print(a)
#二维
b=np.ones((2,5),dtype=int)
print(b)

#empty里面的值是之前存的内存值
a=np.empty(8)
print(a)
b=np.empty((3,4))
print(b)

#linspace创建等差数列def linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None,  axis=0):
print('-'*50)
print('****linspace')
x=np.linspace(1,10,10)
print(x)
print(type(x))
#endpoint是否包含stop
y=np.linspace(5,20,5,endpoint=True)
print(y)

#logspace 创捷等比数列
print('-'*50)
print('****logspace')
x=np.logspace(0,9,10,base=2)
print(x)