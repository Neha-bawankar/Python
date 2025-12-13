#creating dictionary
dict = {
    'name.txt': 'Alice',
    'age': '21',

}
print(dict)
print(dict['name.txt'])

#updating dictionary
dict = {
    'name.txt': 'Alice',
    'age': '21',
}
dict['age'] = '25'
print(dict)


#deleting dictionary
dict = {
    'name.txt': 'Alice',
    'age': '21',

}
del dict['name.txt']
print(dict)
del dict
print(dict)


dict = {
    'name.txt': 'Alice',
    'age': '21',

}
#len()
print("length: %d"  % len(dict))

#str()
print("string: %s" % str(dict))

#type()
print("type: %s" % type(dict))

#clear()
print("clear: %s " % dict.clear()) #take no arguments

dict = {
    'name.txt': 'Alice',
    'age': '21',

}
#copy()
dict2 = dict.copy()
print("Copy dictionary:", dict2)

#fromkeys()
dict = {
    'name.txt': 'Alice',
    'age': '21',

}
dict2 ={'name.txt', 'age', 'gender'}
print(dict.fromkeys(dict2))
print(dict.fromkeys(dict2, 10))

#get()
dict = {
    'name.txt': 'Alice',
    'age': '21',

}
print("name.txt: %s" % dict.get('name.txt'))

#item()
dict = {
    'name.txt': 'Alice',
    'age': '21',

}
print(dict.items())

#keys()
dict = {
    'name.txt': 'Alice',
    'age': '21',

}
print(dict.keys())# take no arguments

#setdefault
dict = {
    'name.txt': 'Alice',
    'age': '21',


}
print(dict.setdefault('gender', None))


#values()
dict = {
    'name.txt': 'Alice',
    'age': '21',


}
print(dict.values())