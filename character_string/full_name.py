first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" #f"{}{}..."可将多个不同变量合并
print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

full_name = "{} {}".format(first_name, last_name)
print(full_name.title())

print("Hi\nBob\nI am Alss!") # \n换行  \t制表符（相当于Tab键）
print("\thi guy!")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

