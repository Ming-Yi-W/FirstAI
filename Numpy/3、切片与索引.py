import numpy as np
'''
    ndarray对象内容可以通过索引或者切片来访问和修改，与python中list的切片操作一样。 
    ndarray数组可以基于0-n的下标进行索引，并设置start，stop以及step参数进行，从原数组中
    切割出一个新数组
'''


#一维数组的切片和索引
print('-'*50)
print('索引操作')
a=np.arange(10)
print(a)

#索引访问，索引从0开始，到长度-1
print('索引0处的索引:',a[0])
print('索引5处的索引:',a[5])

#负索引  倒数第一个索引-1
print('最后一个元素:',a[-1])
print('倒数第三个:',a[-3])



print('-'*50)
print('一维数组切片操作')
#切片操作【start:stop:step】
#什么也没有写的话就是从开始到结尾
print(a[:])
#从索引3开始到结尾
print(a[3:])
#从索引3到索引4[start,stop）
print(a[3:5])
#也可以设置步长,省去的是stop
print(a[3::2])

#切片中负索引
print('一维数组负切片操作')
print(a[::-1]) #反向获取
print(a[-5:-2])


print('-'*50)
print('二维数组中索引操作')

x=np.arange(1,13)
#讲一维数组转换为二维数组
a=x.reshape(4,3)
print(a)
print('获取第二行')
print(a[1])
print('获取第三行第二列')
print(a[2][1])

print('-'*50)
print('二维数组中切片操作')

#[行进行切片,列进行切片]   【start:stop:step,start:stop:step】

#获取所有行所有列
print(a[:,:])
#获取所有行部分列,所有行第二列
print('获取所有行部分列,所有行第二列')
print(a[:,1])
#获取所有行部分列,所有行第一，二列
print('获取所有行部分列,所有行第一，二列')
print(a[:,0:2])

#获取部分行,所有列,奇数列
print('获取部分行,所有列,奇数列')
print(a[::2,:])

#获取部分行，部分列，获取奇数行，第1，2列
print('获取部分行，部分列，获取奇数行，第1，2列')
print(a[::2,0:2])


print('-'*50)
print('坐标获取')
#坐标获取  [行,列]
#获取第2行，第3列的数据
print(a[1][2])
print(a[1,2])

#同时获取不同行不同列，获取第3行第3列，第3行第1列
print('同时获取不同行不同列，获取第2行第3列，第3行第1列')
print(a[1,2],a[2,0])
print(np.array([a[1,2],a[2,0]]))
#使用坐标
print(a[(1,2),(2,0)])

#二维数组负索引的使用
print('二维数组负索引的使用')
print('最后一行')
print(a[-1])
print('行倒序')
print(a[::-1])
print('行列倒序')
print(a[::-1,::-1])