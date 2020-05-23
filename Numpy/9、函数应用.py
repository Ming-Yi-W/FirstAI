import numpy as np
'''
    算数运算：
        如果参与运算的两个对象，都是ndarray,并且形状相同，那么会对位彼此之前进行(+ - * /)运算。
        Numpy算术函数包含简单的加减乘除：add(),substract(),multiply(),divide()0
'''

#三行三列的二维数组
a=np.arange(9).reshape(3,3)
#一维数组
b=np.array([10,10,10])
#当进行相加运算的时候，b会进行广播成三行三列
print('加法')
print(np.add(a,b))
print("-"*50)
print(a+b)



print('减法')
print(np.subtract(a,b))
print("-"*50)
print(a-b)

#out参数的使用
print('out参数的使用')
#dtype不传入默认是float
y=np.empty((3,3),dtype=int)
np.multiply(a,10,out=y)
print(y)

#sin,cos,tan
print('三角函数sin,cos,tan')
a=np.array([0,30,60,90])
print(np.sin(a))

#around(四舍五入) ceil（向上取整） floor（向下取整）
print('around(四舍五入) ceil（向上取整） floor（向下取整）')
a = np.array([1.0,4.55,123,0.567,25.232])
print('arround:',np.around(a))
print('ceil:',np.ceil(a))
print('floor:',np.floor(a))


#聚合函数

print('聚合函数')
a= np.arange(1,13).reshape(3,4)
print('原数组')
print(a)
print('------')

#power中out的使用

print('power中out的使用')
x=np.arange(5)
y=np.zeros(10)
np.power(2,x,out=y[:5])
print(y)

#median()
#一维数组中位数
# 对数组进行排序，数组元素为偶数则是中间两个数的平均值
#如果是奇数，则就是中间那个数
print('median()中位数的使用')
a= np.array([4,3,5,2,1])
print(np.median(a))

#二维数组,要通过axis指定轴
print('二维数组,要通过axis指定轴')
a = np.arange(1,13).reshape(3,4)
print(a)
print('----------')
print('垂直方向',np.median(a,axis=0))
print('水平方向',np.median(a,axis=1))

#mean求平均值
#一维数组
print('mean求平均值')
a= np.array([4,3,5,2,1])
print(np.mean(a))
#二维数组也通过axis求平均
a = np.arange(1,13).reshape(3,4)
print(a)
print('----------')
print('垂直方向',np.mean(a,axis=0))
print('水平方向',np.mean(a,axis=1))

#sum(),max(),min()
print('sum(),max(),min()')
a= np.array([4,3,5,2,1])
print('max:',np.max(a))
print('min:',np.min(a))
print('sum:',np.sum(a))

print('-------')
#argmax , argmin 下标
print('argmax:',np.argmax(a))
print('argmin:',np.argmin(a))
