# The tuple data type is almost identical to the list data type,except in two ways :

# First tuples are typed with parentheses, (and), instead of square brackets, [and].

# But the main way that tuples are different from list is that tuples, like strings, are immutable.Tuples cannot have their values modified, appended or removed.

candies = (10,20,40,'Hey',True,30.5)
print(candies)

print(10 in candies)
print(20 not in candies)
print(candies[0])
print(candies[0:2])
print(type(candies))


# Converting Tuple in List

new_candies = list(candies)
print(type(new_candies))

# Modifying values from the list and then converting list to tupple.
new_candies[1] = 200
new_candies = tuple(new_candies)
print(type(new_candies))