#Creating list
list = ["Apple", "banana", "Cherry", "Mango"]
print(list)

#accessing the list
print(list[2])
print(list[:])
print(list[2:])
print(list[-1])

#updating list
list[3] = "graphes"
print(list)

#deleting
del list[0]
print(list)

#Basic list operations
#len
print(len([1,2,3]))

#Concetenate
list  = [1, 2, 3]
list1  = [4,5,6]
list2 = list +list1
print(list2)

#Repitation
list = ["HII"]
print(list *4)

#in
list = [1, 2, 3]
print(3 in list)



#built-in function and method of list
#len()
list1 = ["Physics", "maths", "english", "che"]
print(len(list1))


#max()
list =[1, 4,8,9]
list1 = ["Physics", "maths", "english", "che"]
print(max(list),max(list1))


#min()
list =[1, 4,8,9]
list1 = ["Physics", "maths", "english", "che"]
print(min(list), min(list1))

'''
#list()
a =(123, 'c++', 'java', 'python')
list1 = list(a)
print(list1)

str = "hello world"
print(list(str))
'''

#append
list1 = ["Physics", "maths", "english", "che"]
list1.append("Hindi")
print(list1)

#count()
list1 = ["Physics", "maths", "english", "che","che"]
print(list1.count("che"))

#extend()
list1 = ["Physics", "maths", "english", "che"]
list2 = [1,2,3,4]
list1.extend(list2)
print(list1)

#index()
list1 = ["Physics", "maths", "english", "che"]
print(list1.index("english"))

#insert()
list1 = ["Physics", "maths", "english", "che"]
list1.insert(3,"Hindi")
print(list1)

#pop
list1 = ["Physics", "maths", "english", "che"]
list1.pop()
print(list1)

#remove()
list1 = ["Physics", "maths", "english", "che"]
list1.remove("english")
print(list1)

#reverse()
list1 = ["Physics", "maths", "english", "che"]
list1.reverse()
print(list1)


#sort()
list1 = ["Physics", "maths", "english", "che"]
