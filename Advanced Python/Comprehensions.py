# List Comprehensions are simply a way to compress a list-building for-loop into a single short, readable line

# This basic yntax of list comphrension is [expression for var in iterable], where
    #  Expression is any valid expression,
    # var is a variable name, and
    # Iterable is any iterable python object.
    


# Write  a python code to create list of square numbers of first 10 numbers

# L = []
# for n in range(11):
#     L.append(n ** 2)
#     print(L)

#      or

# List Comphrensions
square = [n ** 2 for n in range(11)]
print(square)


# Multiple Iterations
demo  = []
for i in range(2):
    for j in range(3):
        demo.append((i,j))
print(demo)

# List Comphrensions

multiple = [(i,j) for i in range(2) for j in range(3)]
print(multiple)

#  Condition on iterator 

# C = []
# for i in range(20):
#     if i % 3 == 0:
#         C.append(i)
#     print(C)

#  or

# List iterator
condition = [i for i in range(20) if i % 3 == 0]
print(condition)


# dictionaries comprehensions

dict = {n : n ** 2 for n in range(5)}
print(dict)

# set Comprehension

set1 = {n ** 2 for n in range(5)}
print(set1)

mod  = [a % 3 for a in range(10)]
print(mod)