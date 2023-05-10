# import legb
# import pypackage.pymodule
#
# print(type(legb), dir(legb))
# legb.func(33)
# print(legb.X)
# pypackage.pymodule.greet('Anna')


# from legb import X, func as legb_func
# from pypackage.pymodule import greet as send_greeting
#
# print(X)
# legb_func(33)
# send_greeting('Anna')


import legb as example_module
import sys
import pypackage.pymodule as mod

print(example_module.X)
print(sys.path)
mod.greet('Anna')
