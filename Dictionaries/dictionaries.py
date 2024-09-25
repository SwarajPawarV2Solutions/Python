#  Dictionary provides a flexible way to access and organize data

# Like a list,a dictionary is a collection of many values. But unlike indexes for lists,indexes for dictionaries can use many different data types, not just integers.

# Indexes for dictionaries are called as keys, and a key with its accociated value is called a key-value pair.

# In code, a dictionary is typed with braces{}

# creating dictionary
myphone = {'brand':'iphone','color':'black','name':'iphone 16 pro max'}
print(myphone)
print(myphone['brand'])
print(myphone['color'])
print(myphone['name'])

# Adding new value in existing dictionary

myphone['price'] = 200000
print(myphone)



# difference between list and dictionary

   #creating list
animal1 = ['dog','cat','tiger','lion']
animal2 = ['tiger','lion','cat','dog'] 
print(animal1 == animal2)  # output will be False. because list checks index wise and not the value wise.     

  # creating dictionary
animal = {'name':'max','age':4}
animal3 = {'age':4,'name':'max'}
print(animal==animal3) # output will be True. because Dictionary checks value wise.If value is present then it returns true




# Methods in Dictionaries
#  values() method
for i in myphone.values():  # This will print in original data type format
 print(i)         # This will print all values from Dictionary.
 
 
#  Keys() method
for n in myphone.keys():      # This will print in original data type format
    print(n)     # This will print all Keys from Dictionary.
 
 
#  items() method
for j in myphone.items():    # This will print in tuple format
    print(j)      # This will print all Key & Value pair from Dictionary.
    

#  in operator in dictionary
print('color' in myphone.keys())   # we need to mention where t search in key or values.

# not in operator in dictionary
print('iphone' not in myphone.values())   # we need to mention where t search in key or values.


print(type(myphone.keys())) # it is of class dict_keys
# Converting dict_keys into list
new_myphone = list(myphone.keys()) 
print(new_myphone)
print(type(new_myphone))  # Now its converted in list

print(type(myphone.values()))  # it is of class dict_values
new_myphone1 = list(myphone.values()) 
print(new_myphone1)
print(type(new_myphone1))  # Now its converted in list



#  Nested Directories

allGuests = {'Ankit': {'samosa': 5,'jalebi':12},
            'vishal': {'chakli':3, 'samosa': 2} ,
            'pranav': {'chiwda': 3,'oreo':1}}

print(allGuests)


