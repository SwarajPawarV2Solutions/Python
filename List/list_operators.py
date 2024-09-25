# List concatination

list1 = [1,2,5,3] + [15,12,8,10,4] # This will join both List
print(list1)



# sort
print(list1.sort())


# List replication

list = ['x','y','z']
print(list)
replicate = list * 3 # replication
print(replicate)


# in operator

print('hello' in ['hello','hey','hi'])  # True
print('car' in ['hello','hey','hi'])  # False
print('hi' in ['hello','hey','hi'])  # True


# not in operator

print('hello'not in ['hello','hey','hi'])  # False
print('car'not in ['hello','hey','hi'])  # True
print('hi'not in ['hello','hey','hi'])  # False


# for loop with list
for num in [0,1,2,3]:
    print(num,end=' ')

print()




# Multiple Assignment

pet = ['Big','Brown','Loud']

# size = pet[0]
# color = pet[1]
# disposition = pet[2]

#       or 

size,color,disposition = pet


print(size,color,disposition)




# print('Enter the name of pet 1:')
# pettName1 = input()
# print('Enter the name of pet 2:')
# pettName2 = input()
# print('Enter the name of pet 3:')
# pettName3 = input()
# print('Enter the name of pet 4:')
# pettName4 = input()
# print('Enter the name of pet 5:')
# pettName5 = input()
# print('Enter the name of pet 6:')
# pettName6 = input()
# print('The names are : ')
# print(pettName1 + ' ' + pettName2 + ' ' + pettName3 + ' ' + pettName4 + ' ' + pettName5 + ' ' + pettName6 )

#            or

petNames = []
while True:
     print('Enter the name of pet ' + str(len(petNames)+1) + '(Or enter nothing to stop.):')
     name = input()
     if name == '':
         break
     petNames = petNames + [name]  # List Concatination
     print('The pet names are : ')
     for name in  petNames:
         print(' ' + name)
         

print(petNames)