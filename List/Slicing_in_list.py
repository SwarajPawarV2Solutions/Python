# Slicing in List

bagpack = ['laptop','pen','notebook','books']
print(type(bagpack),bagpack)

print(bagpack[0:2])  # THis will print values of index 0 and 1 .It will not print the values of Index 2.
# output will be  ['laptop', 'pen']


['laptop', 'pen', 'notebook', 'books']
#   -4       -3       -2         -1    where there is negative value then list indexing starts in reverse order.\
    # In negative case also compiler read list from left to write on indexing start from negative index.

print(bagpack[-1]) # This will print last element in list.

print(bagpack[-3:-1]) # This will print values from  -2 index and -2 index. it will not include -1. It works on reversely.


