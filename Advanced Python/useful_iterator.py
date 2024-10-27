# Useful Iterators

# 1. enumerate
# 2. zip
# 3. map
# 4. filter

bagpack = ['laptop', 'pencil', 'Notebook', 'charger']
print(bagpack)

for i in bagpack:
    print(i)
    

for i in range(len(bagpack)):
    print(i)
    

for i in range(len(bagpack)):
    print(i,bagpack[i])

# enumarate 
for i,val in enumerate(bagpack):
    print(i,val)

# zip
L = [2,4,6,8,10]
R = [3,6,9,12,15]

for lval,rval in zip(L,R):
    print(lval,rval)
# If values are misssing in zip then it will take length as least number.  

A = [2,4,6,8,10]
B = [3,6,9]
# This will print till 6 . 8 and 10 will not printed as there are no values present in B for them.
for Aval,Bval in zip(A,B):
    print(Aval,Bval)


# map : takes a function and applies i to the values in an iterator
# find the first 10 square numbers

square = lambda x: x**2
for val in map(square,range(10)):
    print(val,end=' ')
    

print()
# filter : It only passes-through values for which the filter function evaluates to True

is_even = lambda x: x % 2 == 0
for val in filter(is_even, range(10)):
    print(val,end=' ')
