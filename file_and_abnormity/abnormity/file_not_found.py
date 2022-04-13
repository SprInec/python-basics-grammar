# ------------------------处理 FileNotFoundError 异常----------------------- #
# 使用 try-except 代码块
# alice.py
filename = 'alicek.txt'

"""
打开不存在文件：
with open(filename, encoding = 'uft-8') as f:
	contents = f.read()
"""
try:
	with open(filename, encoding='uft-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")