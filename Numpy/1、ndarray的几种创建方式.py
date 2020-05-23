import  numpy as np


#ndarray类型
a=np.arange(10)
print(a)
print(type(a))


#对列表中得元素开平方（慢）
#对ndarray对象类型进行向量处理
print(np.sqrt(a))

print('***************np中array方法得使用')
#np 得array方法
#array创捷一维数组
a=np.array([1,2,3,4])
print(a)
print(type(a))
#array创捷二维数组
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(type(b))
#array创捷三维数组
b=np.array([[[1,2,3],[4,5,6],[7,8,9]]])

#array中dtype得使用
d=np.array([3,4,5],dtype=float)
print(d)
print(type(d))

#array中ndmin得使用 ,指定维度
e=np.array([3,4,5],dtype=float,ndmin=3)
print(e)

print('-'*50)

print('***************np中arange方法得使用')

#range的使用  range(start,end,step)
a=list(range(1,10))
print(a)

b=list(range(10))
print(b)

c=list(range(1,10,3))
print(c)

#使用arange创建数组  def arange(start=None, *args, **kwargs):
# arange([start,] stop[, step,], dtype=None)
a=np.arange(1,11)
print(a)
#设置步长
b=np.arange(1,11,2)
print(b)
#设置dtype
c=np.arange(2,20,2,dtype=float)
print(c)


print('-'*50)
print('***************np中random方法得使用')
#使用random创建一维数组  数值默认 [0.0, 1.0)
a=np.random.random(size=5)
print(a)
print(type(a))
#创建二维数组,三行四列
b=np.random.random(size=(3,4))
print(b)
#创建三维数组,三行四列
c=np.random.random(size=(2,3,4))
print(c)

#随机整数  randint(low, high=None, size=None, dtype=int)
#一维
a = np.random.randint(6,size=10)
print(a)
#二维
b=np.random.randint(5,11,size=(4,3))
print(b)
#三维
c=np.random.randint(5,11,size=(2,4,3))
print(c)

#其中的dtype属性 默认为int32,可以进行指定
d=np.random.randint(10,size=(5),dtype=np.int64)
print(d.dtype)

#randn函数返回的一个或一组样本，具有标准的正态分布（期望为0,方差为1）
#一维数组长度为4
a=np.random.randn(4)
print(a)
#二维数组2行3列
b=np.random.randn(2,3)
print(b)
#三维数组,两个三行四列
c=np.random.randn(2,3,4)
print(c)

#创建指定方差和期望的正态分布 def normal(loc=0.0, scale=1.0, size=None) 默认为正态
#np.random.normal   参数 loc:期望 scale:方差 size:形状
a= np.random.normal(size=5)
print(a)

#指定方差和期望
b=np.random.normal(loc=2,scale=3,size=(3,4))
print(b)