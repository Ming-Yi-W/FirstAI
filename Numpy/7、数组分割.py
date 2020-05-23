import numpy as np

'''
    numpy.split 函数沿特定的轴将数组分割为子数组，格式如下：
    numpy.split(ary,indices_or_sections,axis)
    参数说明：
        ary:被分割的数组
        indices_or_sections:如果是一个整数，就用该数平均切分，
                            如果是一个数组，为沿轴切分的位置。
        axis:沿着哪个维度进行切向，默认为0，横向切分，为1的时候，纵向切分
'''
print('一维数组')
a=np.arange(1,13)
#调用split函数进行分割
r=np.split(a,4) #默认axis=0
print(r)

print('传递数组  按位置分割')
r=np.split(a,[4,6])
print(r)

print('-'*50)
print('二维数组')
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(a)
print("-"*50)
print('axis=0 水平分割')
r,w=np.split(a,2,axis=1)  #axis=0是横向，1是纵向
print(r)
print("-"*50)
print(w)
print("-"*50)
r,w,k=np.split(a,[2,3],axis=0)
print(r)
print("-"*50)
print(w)
print("-"*50)
print(k)

print('axis=1 垂直分割')
r,w,k=np.split(a,[2,3],axis=1)
print(r)
print("-"*50)
print(w)
print("-"*50)
print(k)


# 使用hsplit()水平方向分隔
print('使用hsplit()水平方向分隔')
r,w=np.hsplit(a,2)
print(r)
print(w)
# 使用vsplit()垂直垂直方向分隔
print('使用vsplit()垂直方向分隔')
r,w=np.vsplit(a,2)
print(r)
print(w)

print('-'*50)
r,w=np.vsplit(a,[2])
print(r)
print('---')
print(w)