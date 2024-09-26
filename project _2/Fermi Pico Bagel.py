
# Step 1
# "Store any number in string format(number to be guessed by player) in a variable `original_number`.

# Step 2
# "Take a number as user input and save it in a variable `guess_number`.(Make sure that the datatype of guess_number is same as of original number i.e- `str`)"

# step 3
# "Check if total number of digits in `original_number` and `guess_number` is not same(Use `len()` function) then ask user for valid input.(First use `len()` to get total digits in `original_number` and `guess_number`.)"

# step 4
# "Using `set()`, check if the digits are repeated in a `guess_number`.
# "Note that datatype `set` allows unique values only.
# "For ex. if `user_input`is 122, then it should print the string 'Duplicate number'  as digit 2 is repeated."

# step 5
# Check winning condition i.e. if both `guess_number` and `original_number` are same, then print 'Fermi' as many number of times as number of digits in a number and print ' You win !! '

# step 6
# "Create empty list called `output` where we will store the output in the form of list.
# "For example: output = [ ' Fermi ', ' Pico ' ,' Pico ' ] ."

# step 7
# Check if any digit and it's position in both `guess_number` and `original_number` are same then append 'Fermi' to `output` list or if only digit matches and not the position then append 'Pico' to `output`

# step 8
# Define a variable called `output_string` which has all values from a list `output` with each value separated by space. (Use 'for' loop to get all the values from a list `output`.)

# step 1
original_number = "123"
while True:
 output = []


# step 2
 guess_number = input("\nGuess the Number:")

# step 3
 if(len(guess_number) != len(original_number)):
    print(f'Enter {len(original_number)} digit number') 
    continue
    
# step 4
 if len(guess_number)  != len(set(guess_number)):
        print('Duplicate number')
        continue
    
# step 5
 if(int(guess_number) - int(original_number)) == 0:
    print('Fermi' *len(original_number))
    print('\nYou Won !!') 
    break

# step 6
 
# step 7
 for i in range(len(original_number)): 
            for j in range(len(guess_number)):     
                if original_number[i] == guess_number[j]: 
                    if i == j:              
                        output.append('Fermi')
                    else:
                        output.append('Pico')
                        

# step 8
 output_string = ''
 for item in output :
        output_string = output_string + ' ' + item

# step 9 
 if len(output) == 0:
    print(' Bagels')
 else:
    print(output_string)