import random, string
length = int(input('Please enter the length you would like your password to be: '))

while length > 50:
    print('This length incorrect')
    length = int(input('Please enter the length you would like your password to be: '))

while length < 0:
    print('This length is too short')
    length = int(input('Please enter the length you would like your password to be: '))

uppercaseChoice = input('Would you like Uppercase letters? (ENTER Yes or No): ')
if uppercaseChoice.upper() == 'YES':
    uppercase = string.ascii_uppercase
elif uppercaseChoice.upper() == 'NO':
    uppercase = ''

lowercaseChoice = input('Would you like lowercase letters? (ENTER Yes or No): ')
if lowercaseChoice.upper() == 'YES':
    lowercase = string.ascii_lowercase
elif lowercaseChoice.upper() == 'NO':
    lowercase = ''

digitsChoice = input('Would you like digits? (ENTER Yes or No): ')
if digitsChoice.upper() == 'YES':
    digits = string.digits
elif digitsChoice.upper() == 'NO':
    digits = ''

specialCharactersChoice = input('Would you like Special Characters? (ENTER Yes or No): ')
if specialCharactersChoice.upper() == 'YES':
    specialCharacters = string.punctuation
elif specialCharactersChoice.upper() == 'N0':
    specialCharacters = ''

generated = ''.join(random.choice(uppercase + lowercase + digits + specialCharacters) for _ in range(length))
print(generated)