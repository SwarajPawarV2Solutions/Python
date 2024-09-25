
# List

list = [1,2,3,4,5]
print(list)

list2 = ['Hello',3.14,50,True,10.5]
print(list2)


bagpack = ['laptop','pen','notebook','books']
print(type(bagpack),bagpack)

print('I have' + ' ' + bagpack[0])
print('I have' + ' ' +  bagpack[1])
print('I have' + ' ' +  bagpack[2])
print('I have' + ' ' +  bagpack[3])

# To get total number of elements in list
print(len(bagpack))


devices = ['laptop',['charger','usb','mouse'] ,'mobile']
print(len(devices))

print(devices[0])
print(devices[1])
print(devices[2])

# To access inner elements of an list
print(devices[1][0])
print(devices[1][1])
print(devices[1][2])


print('I have' + ' ' + devices[1][1])

# This is used to last elements from any list 
print(devices[-1])