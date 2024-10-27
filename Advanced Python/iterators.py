# Iterator is an object that contains a countable number of values
# An iterator is an object that can be iterated upon, meaning that you can traversethrough all the values.
# technically, in python,an iterator is an object which permmits  the iterator protocol, which consists of the methods _iter_() and _next_().


# Iterators

for i in range(10):
    print(i,end=' ')
    
print()

for n in [2,4,6,8]:
    # do some operations
    print(n+1,end=' ')

print()    
print(iter([2,4,6,8,]))

N = 10**12
for i in range(N):
    if i>=10:
        break
    print(i,end=' ')