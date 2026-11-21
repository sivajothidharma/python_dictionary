#Dictionary
#Empty dictionary dict1=dict()
#print(dict1)

dict1=dict(id=2,name='siva',Age=35)
print(dict1)

#zip is a utility function in Python. It allows to compress two tuples
list1=['id','name','Age']
list2=['1','siva','10']
list3=list1+list2 #O/P: ['id', 'name', 'Age', '1', 'siva', '10']
print(list3)
#Zip
z=zip(list1,list2)
print('Zip value of List1 and List2 is: ',z)
#We can't able to get the values directly, Using for loop we can get it
'''
for element in z:
    print(element)
#O/P: ('id', '1')
#('name', 'siva')
#('Age', '10')
'''
dict1=dict(z)
print("The Zip value list1 and list2",dict1)
#O/P: The Zip value dict1 and dict2 {'id': '1', 'name': 'siva', 'Age': '10'}
#Total number of elements:
total=len(dict1)
print("The Zip value list1 and list2",total)
#Convert a dictionary into a set view of keys

print(dict1.keys()) #O/P: dict_keys(['id', 'name', 'Age'])
print(dict1.values()) # O/P: dict_values(['1', 'siva', '10'])
print(dict1.items()) #o/p: ict_items([('id', '1'), ('name', 'siva'), ('Age', '10')])
for element in dict1:
    print(element)
#O/P: id
#name
#Age
#Extracting the items from a dictionary into a set view of values
#Each Key and value pair is the tuples

for key,value in dict1.items():
    print(key,value)
# O/P: id 1
# name siva
# Age 10

#Highest Value (Many character)
#highest=max(dict1,key=dict1.get) #O/P: The highest value is:  name
highest=max(dict1.items(),key=lambda item: item[0]) #O/p: ('name', 'siva')
print("The highest value is: ",highest)

#minimum value
lowest=min(dict1,key=dict1.get)
print(lowest)
#Sorting of dictionary
#list2=sorted(dict1.values()) #O/P: ['1', '10', 'siva']
list2=sorted(dict1.items(),key=lambda item: item[0],reverse=True) #O/P:[('Age', '10'), ('id', '1'), ('name', 'siva')]
print(list2)

