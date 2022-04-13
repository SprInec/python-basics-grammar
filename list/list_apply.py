name = ['Bob', 'Xiaoming', 'Dalei']
print(name[0])
print(name[1])
print(name[2])

message1 = f"{name[0]}:\n\tI bless you happy forever!"
print(message1)
message2 = f"{name[1]}:\n\tI bless you young forever!"
message3 = f"{name[2]}:\n\tI bless you rich forever!"
messages = [message1, message2, message3] #列表可嵌套

print(messages[2]) 

#-------------------修改列表某个元素的值-------------------#
#不可用于空列表
name[0] = 'Alice'
print(name[0])
print(name)

#------------------附加某个元素到列表末尾------------------#
#方法 append()
name.append('Bob')
print(name)

list1 = [] #可用于空列表
list1.append('1')
list1.append('2')
list1.append('Alice')
print(list1)

#----------------------在列表插入元素---------------------#
#方法 insert()
list1.insert(0, '0')
print(list1)

list2 = [] #可用于空列表
list2.insert(0, '0')
list2.insert(1, '1')
print(list2)

#--------------------从列表中删除元素---------------------#

#语句 del 
#前提：知道要删除元素索引
#效果：删除后不可再访问其值
number = ['0', '1', '2']
del number [0]
print(number)

#语句 pop()
#效果：从A列表中删除元素并移入B列表
list3 = ['A', 'B', 'C']
list4 = list3.pop() #括号内为void默认删除末尾元素
print(list3)
print(list4)

list3.append('D')
list4 = list3.pop(1)
print(list3)
print(list4)

list5 = [] #也可用一个列表存储pop()移出的元素
list5.append(list3.pop(1))
print(list5)
print(list3)
list5.append(list3.pop(0))
print(list3)
print(list5)

#方法 remove()
#条件：只知道要删除元素的值
#效果：根据值删除元素
list6 = ['A', 'B', 'C']
list6.remove('A')
print(list6)

