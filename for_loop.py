# We have range function in python range()

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

# range(0,10,2)  0 = start , 10 = end , 2 = step parameter


# for loop

print("My name is :")
for i in range(5):
    print("Swaraj (" + str(i) + ")")
    


# equivalent code for while loop

print("My name is :")
i = 0
while i< 5:
        print("Swaraj (" + str(i) + ")")
        i = i + 1
        
        

# Range function

for i in range(10,15):
  print(i)
  
  
  # using step parameter in range function (we are using 2 as step parameter)

for i in range(10,15,2):
  print(i)
  
  
# this will print 0 to 10 in reverse order
for i in range(10,-1,-1):
  print(i)
  
  
total = 0
for num in range(11):
    total = total + num
print(total)