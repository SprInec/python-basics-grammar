# ------------------------导入类---------------------------#
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# -----------------在一个模块中存储多个类------------------#
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# -----------------从一个模块中导入多个类-------------------#
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# ----------------------导入整个模块-------------------------#
import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# ---------------------导入模块中所有的类--------------------#
# 语法 form module_name import *
from car import *

# -----------------在一个模块中导入另一个模块-----------------#

# -------------------------使用别名---------------------------#
from car import ElectricCar as EC

# --------------------自定义工作流程--------------------------#

