
# Step 1
# "Store any number in string format(number to be guessed by player) in a variable `original_number`.

# Step 2
# "Take a number as user input and save it in a variable `guess_number`.(Make sure that the datatype of guess_number is same as of original number i.e- `str`)"

# step 3
# "Check if total number of digits in `original_number` and `guess_number` is not same(Use `len()` function) then ask user for valid input.(First use `len()` to get total digits in `original_number` and `guess_number`.)"



# step 1
original_number = "123"
print(type(original_number))
original_num_len = len(original_number)
print("Guess the Number")

# step 2
guess_number = str(input())
print(type(guess_number),guess_number)

# step 3
if(len(original_number) != len(guess_number)):
    print("Enter valid Input of", original_num_len , "digit") 
    guess_number = str(input())