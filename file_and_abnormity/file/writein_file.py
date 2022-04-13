# --------------------------写入文件---------------------------# 
# --------------写入空文件------------ #
# write_message.py
filename = 'programming.txt'

"""
   调用函数 open() 时可指定第二个实参:
   'w' 写入模式 (注意:以此模式打开已存在文件会先清空文件内容)
   'r' 读取模式
   'a' 附加模式
   'r+' 读写模式 
   若省略的模式实参，Python将以默认只读模式打开文件
"""
"""
   Python只能将字符串写入文本文件中。
   要将数值数据存储到文本文件中，必须先用函数 str() 将其转换为字符串格式。
"""
with open(filename, 'w') as file_object:
	file_object.write("I love programming.")

# ----------------------- 写入多行------------------------------ #
# write()不会在写入文本末尾自动添加换行符
# 要让每个字符串都单独占一行，需要在方法调用write()中包含换行符
filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

# ----------------------- 附加到文件------------------------------ #
# 如果要给文件添加内容，而不是覆盖原有内容，可以以附加模式打开文件
filename = 'programming.txt'

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")


