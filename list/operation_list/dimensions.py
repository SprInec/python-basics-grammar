#-------------------------------------元组---------------------------------------#
#不可变的列表
#定义时用 () ,索引时用 []
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# X dimensions[0] = 1 #试图修改元组的操作被Python所禁止

#严格来说，元组是由逗号所定义的，()只是为了使其看起来更整洁、清晰
dimensions = 100, 20
print(dimensions[0])
dimensions = 3,
print(dimensions)
print(dimensions[0])

#--------------遍历元组--------------#
dimensions = (1, 2, 3, 4)
for dimension in dimensions:
	print(dimension)

#-------------修改元组变量------------#
#给原先元组重新赋值
dimensions = (1, 2)
dimensions = (2, 3)

#test
#除了不可修改元组元素，也不可增加、删除元素
# X dimensions.append(4)
# X del dimensions[1]


