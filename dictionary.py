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
#Access an element
#Set and Dict doesn't have the indexing
value=dict1['id']
print("The ID is: ",value)

#Insert an element
dict1['gender']='male'
dict1['salary']='10000'
dict1['Age']='20' #Insert the value
dict1.update({'Age':'30'}) #Update the value in the middle
dict1.pop('Age') #Delete the item based on Item. Bydefault it delete the last item in the dictionary
print("The dict1 is: ",dict1)

#Create/Copy the dict
dict2=dict1.copy()
print("The dict2 is: ",dict2)
#fromkeys
list1=['Siva','Thamizhi','Kanimozhi']
projectcode="Employess"
dict5={}
dict2=dict1.fromkeys(list1,projectcode)
#O/P: The fromkeys are  {'Siva': 'Employess', 'Thamizhi': 'Employess', 'Kanimozhi': 'Employess'}
print("The fromkeys are ",dict2)

#Convert string into multiple strings
str1=("Siva=10,Thamizhi=20,Thamizhi=25,Kanimozhi=40")
print("The Original Data",str1)
list4=str1.split(",") #o/p: ['Siva=10', 'Thamizhi=20', 'Thamizhi=25', 'Kanimozhi=40']
print("Splited the data comma(,) basis",list4)
for item in list4:
    x=item.split('"=')
    print("The Split value is ",x)
    list3.append(x)
    print("The Split value of list3 is  ",list3)
#O/P: The Split value of list3 is   ['id', 'name', 'Age', '1', 'siva', '10', ['Siva=10'], ['Thamizhi=20'], ['Thamizhi=25'], ['Kanimozhi=40']]
'''
count=0
for key,value in list1:
    list1[count]=[value,key]
    count+=1
    print("The Count value of list1 is  ",list1)

'''

