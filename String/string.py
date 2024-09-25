name = 'Swaraj'

print(len(name))
print(name[0])
print(name[-1])
print(name[0:4])
print('p' in name)
print('w' in name)
print('w'not in name)
print('p'not in name)
for i in name:
    print('*****' + i + '*****')  
    
new_name = name[0:4] + 'a'+ name[5:]
print(new_name)