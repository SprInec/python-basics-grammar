#-------------------------------if 语句简单示例-------------------------------#
cars = ['audi', 'bmw', 'subaru', 'toyota']

#------------------相等判断-----------------#
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# if 语句判断时区分大小写
car = 'Audi'
if car == 'audi':
    print("True")
else:
    print("False")

#若大小写无关紧要，可用方法 lower() 将变量转换为小写后进行 if 判断
if car.lower() == 'audi':
    print("Ture")
else:
    print("False")

#-------------------不等判断--------------------#
requested_topping = 'mushrooms'#(蘑菇)

if requested_topping != 'anchovies':#(意式小银鱼)
    print("Hold the anchovies!")

#--------------------数值比较-------------------#
age = 17
if age != 18:
    print("That is not the correct answer, try again！")
age > 18
age < 18
age >= 18
age <= 18

#------------------检查多个条件-------------------#
# and 
age = 19
if age > 18 and age < 60:
    print("OK! You are allowd to access.")

# or
age = 19
if (age < 20) or (age > 40):
    print("OK!")

#--------------检查特定值是否包含在列表中-------------#
# 使用关键字 in
requested_topping = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_topping:
    print("True")

#------------检查特定值是否不包含在列表内-------------#
# 使用关键字 not in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

#----------------------布尔表达式----------------------#
#术语 布尔表达式 -> 条件测试的别名
game_active = True
can_edit = False

#--------------------------------Exercise-------------------------------------#
car = 'subru'
print("Is car == 'subare'? I predict True." )
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
