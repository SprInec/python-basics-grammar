#-------------使用方法 sort() 对列表永久排列--------------#
#特性：按字母顺序永久排列， 无法恢复到原来的排列顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
print(cars)

cars.sort(reverse = True)  #按与字母顺序相反顺序排列,sort()参数中输入 reverse=True
print(cars)

#------------使用函数 sorte() 对列表临时排序---------------#
#特性：保留原来的排列顺序，同时以特定的顺序呈现
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print(sorted(cars, reverse = True)) #与字母顺序相反排序

#--------------使用方法 reverse() 倒着打印列表---------------#
#特性：永久性反转列表打印顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()
print(cars)

#--------------使用函数 len() 确定列表的长度------------------#
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(len(cars))

