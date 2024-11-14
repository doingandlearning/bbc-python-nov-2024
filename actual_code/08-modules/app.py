import utils as u  # alias whole modules
# import numpy as np
# import pandas as pd
import random
from random import choice
import sys

print(sys.platform)
# from utils import Shape # you can alias this as well!
#
#
# triangle = Shape("triangle")  # namespacing ...
#
# u.printer(triangle)
#
# print(triangle == u.default_shape)
# print(f"The name of app.py is {__name__}")

print(random.randint(1,6))
food_options = ["Chinese", "Thai", "Burgers", "Popeyes", "Pizza", "Nandos"]
print(choice(food_options))

print(food_options[random.randint(0, len(food_options) - 1)])

print(max([1, 2, 3,4,5,6]))