#列表，类似于C语言中的数组和结构体的杂糅
#可以存放一系列按特定顺序排列的元素，注意：其中元素可毫无关系
bicycle = [100, 'trek', 'cannondale', 'redline', 'specialized', 1.0, 2]
print(bicycle) 
print(bicycle[0])
print(bicycle[3].title())
print(bicycle[-1])  #通过将索引指定为-1可直接访问列表最后一个元素
print(bicycle[-2])  #负数索引也可用于访问倒数第n个元素