#SIMPLE SECURE PASSWORD GENERATOR -LUDWIG PELAEZ
import random
while True:
    print('-----------------------------------------------')
    print('WELCOME TO THIS ULTRA SECURE  PASSWORD GENERATOR')
    print('-----------------------------------------------')
    print('')
    low_char= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cap_char= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    number=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbol=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', ':', '<', '>', '?', ',', '.', '/']
    all_char= low_char + cap_char + number + symbol
    length=int(input('How many characters would you like your password to have? \n'))
    password = ''.join(random.choice(all_char) for i in range(length))
    print('Your password is: ', password)  # Print the generated password
    print('')  # Empty line for better readability
    print('-----------------------------------------------')
    cont=input('Would you like to generate another password? (y/n) \n')
    print('-----------------------------------------------')
    if cont.lower()=='n':
        break
    else:
        continue
# Print a message to thank the user for using the password generator 
print('********************************************************')
print('THANK YOU FOR USING THIS ULTRA SECURE PASSWORD GENERATOR')
print('********************************************************')  