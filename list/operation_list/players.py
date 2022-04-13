#----------------------------------使用列表的一部分---------------------------------#
#--------------------切片------------------#
players = ['charles', 'martina', 'michael', 'florence', 'eli']
#可指定要使用的第一个元素和最后一个元素+1的索引：
print(players[0:3])
print(players[2:4])

#若没有指定第一个索引，Python将自动从列表开头开始：
print(players[:4])

#若没有指定第二个索引，Python将默认到列表末尾结束：
print(players[2:])

#该方法也可用于负数索引
print(players[-2:])

#若指定的第二个索引超过列表中元素个数,将截取到末尾元素结束：
print(players[3:7])
print(players[:7])

#若列表为空列表，切片后也为空列表
number = []
print(number[1:2])

#也可在切片方括号中指定第三个值，为本次切片的步长：
print(players[0:4:2])

#------------------遍历切片-------------------#
print("Here are the first three players on my team:")
for player in players[0:3]:
	print(player)

#------------------复制列表(得到两个列表)--------------------#
#同时省略切片的起始索引和终止索引
date = [1, 2, 3, 4, 5, 6, 7, 8]
copy = date[:]
print(copy)

#test 列表覆盖
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1 = list2[:]
print(list1)

#-------------链接两个列表(本质上还是同一个列表)--------------#
data = [1, 2, 3]
copy = data
print(copy)
data.append(4)
print(copy)