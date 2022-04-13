# -----------------------函数 input() 工作原理--------------------#
# input() 会使程序暂停，等待用户输入一些文本，并看作为字符串
message = input("Tell me something, and I will repeat it back to you:")
print(message)

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
# ---- += ----- #
# 可用于多行输入字符串

name = input(prompt)
print(f"Hello, {name.title()}!")