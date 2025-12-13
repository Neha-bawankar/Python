
#global variable or namesapce
'''var1 = 5
def scope_fun():
    #local variable
    var2 =  10
    def scope_fun3():
        print("Hiii")
    scope_fun3()
scope_fun()
'''

'''Money = 2000
def AddMoney(Money):
    Money1 = Money +1
    print(Money1)
res = AddMoney(5000)
print(res)

'''
''''
#dir  // No Space parameter
print((dir))
import random
print(dir(random))

#Method Object
import random
print("Attribute of the random number")
print(dir(random))

#List arribute of dir function
list = ['Hello', 'I', 'Am']
d = {}
print(dir(list))
print(dir(d))'''

x = 10


def my_function():
    pass


import math

print(dir())

my_list = [1, 2, 3]
print(dir(my_list))

import os

print(dir(os))


class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


my_instance = MyClass(5)
print(dir(my_instance))











global_var = 10

def my_function():
    print("Inside function, globals():", globals()['global_var'])
    globals()['new_global_var'] = 20 # Modifying global namespace

my_function()
print("Outside function, global_var:", global_var)
print("Outside function, new_global_var:", new_global_var)


def my_function2():
    a = 10
    name = "Attribute"
    print("Inside local Variable: ", locals())
    locals()['New_key_value'] = 10
my_function2()

