"""x = 1"""
"""while x <= 500:
    print("hello world", x)
    x += 1
   """
# break keyword
"""while x <= 5:
    print("hello world")
    #x += 1
    if x == 3:
        break
"""
"""while x <= 10:
    print(x)
    x += 1
 """
# else keyword
"""count = 0
while count <5:
    print(count, "is less than 5")
    count = count +1
else:
    print(count, "is not less than ")
"""

# single statements
"""flag = 1
while(flag): print("given falg is really true")
"""

# for loop
"""fruits = ["apple", "mango","cherry"]

for fruit in fruits:
    print(fruit)


range(5)
for var in (range(5)):
    print(var)

for letter in 'Python':
    print(letter)




number = [1, 2, 3, 4, 5, 6,]
for num in number:
    if num%2 ==0:
        print("The list contain an even number")
        break

    else:
        print("The list does not contain even number")


for i in range(1, 11):
    for j in range(1, 11):
        k = i*j
        print(k)
"""



# nested loop

"""for i in range(1, 5):
    star=""
    for j in range(i):
        star += "*"
print(star)

for i in range(1, 11):
     for j in range(1,11):
         k = i*j
         print(k, end=" ")
"""


# break statement
"""for number in range(10):
    if number == 5:
        break
    print(number)

for letter in 'python':
    if letter == 'h':
        break
    print(letter)
  """

# continue statement
"""for number in range(10):
    if number == 5:
        continue
    print(number)
"""
# pass statement
'''for number in range(10):
    if number == 5:
        pass
    print(number, end= " ")
'''
"""
fruits = ['Apple', 'banana', 'mango']
for fruit in fruits:
    print(fruit)


for number in range(1, 5):
    print(number)

for i in 'Pyhton':
    print(i)


list =[1, 2, 3, 4, 5]
sum =0
for num in list:
    sum += num

    print(sum)

number =[1, 2, 3, 4, 6, 8]
for i in number:
    if i%2 ==0:
        print("even")
    else:
        print("Not even")


for i in range(5,6):
    for j in range(1, 11):
        k = i*j
        print(k)

for num in range(1, 10):
    if num ==5:
        continue
    print(num)

# print pyramid
for i in range(1, 5+1):

    for j in range(5-1):
        print(" ", end ="")
    for k in range(2 *i - 1):
        print("*",end ="" )
    print()

#

"""
'''
# indexing or slicing
var1 = "Hello world"
print(var1)
print(var1[:5])
print(var1[2:])

#updating string
var2 = "Good morning"
print(var2 + " All")
print(var2[2:5] + "hello")
'''

#concatinate
'''
name.txt = "Vipul"
surname = " Sharma"
print(name.txt + surname)


print("Vipul" + " Sharma")

age = 25
print("Vipul age is "+ str(age))

name.txt = "Neha"
age = 23
print(name.txt + " age is " + str(age))

age = 35
name.txt = "sharmaji"
city = "Indore"

print(f"{name.txt} which is age is {age} live in {city}")


# Repitition

print("python" * 3)
print("py" *3 + "Thon" *3)
'''

# String method
#capitalize
s = "i am LEARNING Python LanGuage"
res = s.capitalize()
print(res)

s = "123hello WOrld"
res = s.capitalize()
print(res)

#center
s = "hello"
res = s.center(20, ".")
print(res)


#count
s = 'hello world'
res= s.count('o')
print(res)

s = "this is string example.... wow !!"
sub = 'i'
print("str.count(i):-", s.count(sub))
sub = "exam"
print("str.count('exam', 10, 2:", s.count(sub,3, 25))

# len
s = "I am learning python "
res = len(s)

print(res)

#index
s1 = "This is string example"
s2 = 'exam'
res = len(s1)
print(res)
print(s1.index(s2))
print(s1.index(s2, 10))
print(s1.index(s2, 10, 40))


# isalnum()
s1 = "1234isaalphanumericcharacter"# no space in this string
res = (s1.isalnum())
print(res)


#isalpha()
s1 ="hii"
res = s1.isalpha()
print(res)

#isdigit()
s1 = "2"
res = s1.isdigit()
print(res)


#islower()
str= "This Is the LowerCase method"
res =str.islower()
print(res)

#isnumeric()
str = "123"
res = str.isnumeric()
print(res)

#isspace()
str ="   "
res= str.isspace()
print(res)

#istitle()
str = "This Is The Title Method"
res = str.istitle()
print(res)

#isupper()
str = "THIS IS THE UPPER METHOD "
res = str.isupper()
print(res)


#JOIN
str ="-"
li = 'apple', 'banana', 'mango'
print(str.join(li))

#ljust
str = "THIS IS THE UPPER METHOD "
print(str.ljust(50, "-"))

#lower()
str = "THIS IS THE UPPER METHOD "
res = str.lower()
print(res)

#lstrip()
str =  "      This is my string     p"
res = str.lstrip()
print(res)


#rstrip()juu
str ="      This is my string p! ******"
res = str.rstrip("*")
print(res)


#strip()
str ="********* This is my string p! ******"
res = str.strip("*")
print(res)

#maketrans()
str = "This as my string"
intab ="aeiou"
outab ="12345"
trantab = str.maketrans(intab, outab)
print(str.translate(trantab))


name =  "Python"

if name == "java" or "html":
    print("login successful")
else:
    print("authentication failed")

#startwith()
str = "This as my string"
res = str.startswith("This")
print(res)


#endwith()
str = "This as my string !!!!"
res = str.endswith("!!!")
print(res)

#expandtab \t
str = "This\tas my string !!!!"
res = str.expandtabs()
print(res)

#find
str = "This as my string !!!!"
str2 ="my"
print(str.find(str2))

#max()
str = "This as my string"
res = max(str)
print(res)

#min()
str = "THISISTHEMYSTRING"
res = min(str)
print(res)

#replace
str = "This as my string"
print(str.replace("as", "is"))

#rfind()
str ="This is really a string example"
str1 = "is"
print(str.rfind(str1))
print(str.rfind(str1,10, 0))

#rjust
str ="This is really a string example"
res = (str.rjust(50,"*"))
print(res)

#split()
str ="This is really a string example"
res = str.split()
print(res)

#splitlines()
str ="This is \nreally a string example"
print(str.splitlines())


#encode()
import base64

str = "this is string example"
str =base64.b64encode(str.encode('utf-8',errors='strict'))
print(str)

#decode
"""str = "this is string example"

print(str.decode('base64', 'strict'))"""


#rindex
str = "this is string example"
str1 ="is"
print(str.rindex(str1))


#swapcase()
str= "this is string example"
str2="THIS IS STRING EXAMPLE"
res = str2.swapcase()
print(res)

#title()
str= "this is string example"
res= str.title()
print(res)

#zfill()
str= "this is string example"
res = str.zfill(50)

print(res)

#upper()
str= "this is string example"
res = str.upper()
print(res)

#isdecimal()
str= "123345"
res = str.isdecimal()
print(res)