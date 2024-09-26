
# Set contains unordered collections of unique items.They are defined much like lists and tuples, except they use the curly brackets of dictionaries,{}

# sets
primes = {2,3,5,7}
odd = {1,3,5,7,9}
print(type(primes), primes)
print(type(odd),odd)

# Union: items appearing in either

primes | odd  # with an operator
print(primes.union(odd))  # equivalently with a method


# Intersection: items appearing in both

primes | odd
print(primes.intersection(odd))  # Intersection() method prints common number which are present in both sets

# Difference: items in primes but not in odd
primes - odd
print(primes.difference(odd)) # it will print only the value which is not present in odds. that is 2.


#Symmetric difference

primes ^ odd
print(primes.symmetric_difference(odd)) # It cancels common values from both sets and give remaining values which is not common in both sets.