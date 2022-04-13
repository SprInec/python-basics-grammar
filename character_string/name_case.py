name = "eric"
print(f"Hello {name.title()}, would you like to learn some Python tody?")

print(name.title()) #将首字母大写，其余小写
print(name.upper()) #将所有字母大写
print(name.lower()) #将所有字母小写

name = "龙应台"
sentence = '"人生像条大河，可能风景清丽，更可能惊涛骇浪。\n你需要的伴侣，最好是那能够和你并肩立在船头，\n浅斟低唱两岸风光，同时更能在惊涛骇浪中紧紧握住你的手不放的人。\n换句话说，最好她本身不是你必须应付的惊涛骇浪。"'
print(f"{name}先生曾说过：{sentence}")

name = " Bob "
print(name.lstrip()) #删除开头空格
print(name.rstrip()) #删除末尾空格
print(name.strip())  #删除开头和末尾空格