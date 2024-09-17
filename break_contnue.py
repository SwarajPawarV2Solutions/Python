# Break Statement 

# The break statement is used to terminate the loop immediately when it is encountered.
# We can use the break statement with the for loop to terminate the loop when a certain condition is met.


for n  in range(20):
    if n % 2 == 0:
        print(n,end=" ")
        
        
print()
        
for n  in range(20):
    if n % 2 == 0:
        print(n,end=",")
    if n == 10:
        break


print()
    
for n  in range(20):
    if n % 2 == 0:
      if n == 10:
        break
      print(n,end=",")