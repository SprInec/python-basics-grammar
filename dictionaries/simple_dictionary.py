#------------------------一个简单的字典----------------------------#
#字典是一系列的键值对
#字典中可包含任意数量的键值对
#键与键之间用'，'分开
#键与值之间用': '分开
#可将Python中的任何对象作为字典中的值，包含但不局限于数、字符串、字典
alien_0 = {'color': 'green', 'points': 5}

#访问字典中的值，会返回与键相关联的值（如下↓）
print(alien_0['color'])
print(alien_0['points'])

#应用
new_points = alien_0['points']
print(f"You have got {new_points} points!")

#字典是一种动态结构，可随时向其中添加键值对
#字典中元素的排列顺序与添加顺序相同
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#--------------创建一个空字典---------------#
#注意：字典用的是 {} 括号
#注意：列表用的是 [] 括号
alien_1 = {}

#依次向其中添加元素
alien_1['color'] = 'green'
alien_1['points'] = 5

print(alien_1)

#---------------修改字典中的值---------------#
#将颜色改为黄色
alien_1['color'] = 'yellow'
print(alien_1['color'])

#------------------有趣的例子-----------------#
#对一个能够以不同速度移动的外星人进行位置跟踪
alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x_position: {alien_2['x_position']}")

#向右移动外星人
#根据当前速度确定将外星人向右移动多远
if alien_2['speed'] == 'slow':
	x_increment = 1
elif alien_2['speed'] == 'medium':
	x_increment = 2
else:
	#这个外星人移动的速度肯定很快
	x_increment = 3

#新位置为旧位置加上移动距离
alien_2['x_position'] = alien_2['x_position'] + x_increment

print(f"New x_position: {alien_2['x_position']}")

#-------------------删除键值对-------------------#
#使用 del 语句
alien_3 = {'color': 'green', 'points': 5}

#使用 del 语句时必须指定字典名和要删除的键
del alien_3['points']
print(alien_3)

#---------------由类似对象组成的字典--------------#
#可用于储存诸多对象的同一信息
favorite_language = {
	'jen': 'python',
	'sarah': 'C',
	'edward': 'ruby',
	'phil': 'Python',
	}

#----------------使用 get() 来访问值---------------#
# get() 第一个参数用于指定键
# get() 第二个参数(可选)为指定的键不存在时要返回的值
alien_4 = {'color': 'green', 'speed': 'slow'}

point_value = alien_4.get('point', 'No point value assigned.')
print(point_value)

# 若 get() 没有指定第二个值且指定的键不存在，Python将返回值 None
# None并非错误，而是一个表示所需值不存在的特殊值
point_value = alien_4.get('point')
print(point_value)

