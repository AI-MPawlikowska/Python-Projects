letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random
print("PyPASSWORD Generator")
print('''

              ,;;;,
             ;;;;;;;
          .-'`\, '/_
        .'   \ ("`(_)
       / `-,.'\ \_/
       \  \/\  `--`
        \  \ \
         / /| |
        /_/ |_|
    ( _\ ( _\  #:##        #:##        #:##         #:##
                        #:##        #:##        #:##
''')

print("Welocome to the PYPASSWORD Generator!")
nr_letters=int(input("How many letters wold you like in your password?\n "))

nr_numbers=int(input("How many symbols wold you like in your password?\n "))

nr_symbols=int(input("How many numbers wold you like in your password?\n "))


print("Your password is:\n ")


password = ""
for char in range (1, nr_letters +1):
    password += random.choice(letters)


for char in range (1, nr_numbers +1):
    password += random.choice(numbers)

for char in range (1, nr_symbols +1):
    password += random.choice(symbols)

print(password)
