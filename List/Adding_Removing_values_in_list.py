#  Adding Values in List

# append() method is used to add new values to the list.The append() method call adds the argument to thre end of the list 

bagpack = ['laptop','laptop','pen','notebook','books']
print(type(bagpack),bagpack)

bagpack.append('pen')  # 'Pen' will add at last position in the list.
print(bagpack)

bagpack.append('water bottle')  # 'water bottle' will add at last position in the list.
print(bagpack)

# insert() method can insert a value at any index in the list. The first argument to insert() is the index for the new value, and the second argument is the new value to be inserted. 


bagpack.insert(0,'First Element') # Insert method will add given string at given index.
print(bagpack)

# Deleting Values in the List

# del statement will delete values at an indexin a list. All of the values in the list after the deleted values will be moved up one index

del bagpack[-1]
print(bagpack)

# remove() method is passed the value to be removed from the list it is called on. Attempting to delete  a value which does not exist in the list  will result in a ValueError. If the value appears multiple times in the list, only the first instance of the value will be removed.

bagpack.remove('laptop')
print(bagpack)