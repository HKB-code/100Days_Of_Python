import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = ""
for letter in range(1,nr_letters+1):
    password += random.choice(letters)
password = list(password)

for symbol in range(1,nr_symbols+1):
    password += random.choice(symbols)
    
for number in range(1,nr_numbers+1):
    password += random.choice(numbers)

# give error because it return none(random.shuffle)
# new_password = "".join(random.shuffle(password))
random.shuffle(password)
new_password = "".join(password)
print(new_password)


# The shuffle() method takes a sequence, like a list, and reorganize the order of the items.

# Note: This method changes the original list, it does not return a new list.



# The join() method takes all items in an iterable and joins them into one string.
# string.join(iterable)
# A string must be specified as the separator.