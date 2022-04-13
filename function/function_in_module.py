# -------------------------将函数存储在模块中------------------------ #
# import 语句允许在当前运行的程序文件中使用模块中的代码

# ------------导入整个模块---------- #
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green poppers', 'extra cheese')

# -----------导入特定的函数---------- #
# 格式： 
"""      form module_name import function_0, function_1, function_3    """
# 使用这种语法时，调用函数不用使用 ' . ' 

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green poppers', 'extra cheese')

# ----------使用 as 给函数指定别名---------- #
# 格式：
"""       form module_name import function_name as fn     """

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green poppers', 'extra cheese')

# ----------使用 as 给模块指定别名----------- # 
# 格式：
"""       import module_name as mn       """

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green poppers', 'extra cheese')

# --------------导入模块中的所有函数-------------- #
# --------使用（ * ）运算符可以让Python导入模块中的所有函数
# 格式：
"""        form module_name import *         """
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green poppers', 'extra cheese')