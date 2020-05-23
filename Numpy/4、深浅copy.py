import numpy as np

#创建一个二维数组
a=np.arange(1,13).reshape((3,4))
print(a)
#对a数组进行切片处理，获取第一，二行，第一，二列
sub_a=a[:2,:2]
print(sub_a)
#对sub_a中第一行第一列的值进行修改
sub_a[0][0]=100
#这是一个浅拷贝
#通过切片可以获取到新的数组，即使赋值给新的变量，但还是原来数组的视图
#如果对切片数组中元素的值进行修改,会影响原来数组。
print('这是一个浅拷贝')
print(sub_a)
print(a)

print('-'*50)
print('可以使用numpy中的copy方法实现深拷贝')
#可以使用numpy中的copy方法实现深拷贝
sub_bb=np.copy(a[:2,:2])
sub_bb[0,0]=200
print(sub_bb)
print(a)