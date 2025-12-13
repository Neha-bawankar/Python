def fun(first_name, last_name, city):
    print("hello, world")
    print(f"I am {first_name} {last_name}")
    print(f"I am from {city}")


fun("Neha", "Bawankar", "Nagpur")
fun("Akshita", "A", "Bengaluru")


def add(a, b):
    return (a + b)

    print("Hii")


res = add(3, 4)
print(res)


#Required

def fun1(str, num):
    print(str, num)


fun1("hII", 8)


# KEYWORD Argument
def fun2(name, age):
    print("name.txt : ", name)
    print("age :", age)


fun2('Aman', 29)


#default
def fun3(name, age=35):
    print('name.txt:', name)
    print('age: ', age)


fun3("Rahul")


#positional
def fun4(name, age, city):
    print(name, age, city)


fun4("Naman", "indore", 10)


#arbitary function
def fun5(*args, **kwargs):
    print("args function:")
    for arg in args:
        print(arg)

    print("kwargs function")
    for key, value in kwargs.items():
        print(f"{key} ={value}")


fun5("hii, i am naman", first_name='Nman', last_name="Singh")

#anomyous
def cube(x):

    return x*x*x

res = cube(5)
print(res)


cube1= lambda x : x*x*x
res =cube1(5)
print(res)

#inner function
def f1():
    print('Hello')
    def fun2():
        print("I am naman")
    fun2()
f1()

