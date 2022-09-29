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
    strength = 1
elif uppercaseChoice.upper() == 'NO':
    uppercase = ''
    strength = 0

lowercaseChoice = input('Would you like lowercase letters? (ENTER Yes or No): ')
if lowercaseChoice.upper() == 'YES':
    lowercase = string.ascii_lowercase
    strength1 = 1
elif lowercaseChoice.upper() == 'NO':
    lowercase = ''
    strength1 = 0

digitsChoice = input('Would you like digits? (ENTER Yes or No): ')
if digitsChoice.upper() == 'YES':
    digits = string.digits
    strength2 = 1
elif digitsChoice.upper() == 'NO':
    digits = ''
    strength2 = 0

specialCharactersChoice = input('Would you like Special Characters? (ENTER Yes or No): ')
if specialCharactersChoice.upper() == 'YES':
    strength3 = 1
    specialCharacters = string.punctuation
elif specialCharactersChoice.upper() == 'N0':
    strength3 = 0
    specialCharacters = ''


total_strength = strength + strength1 + strength2 + strength3

if total_strength == 1:
    print('You password strength is very weak!')

elif total_strength == 2:
    print('You password strength is weak!')

elif total_strength == 3:
    print('Your password strength is strong!')

elif total_strength == 4:
    print('Your password strength is very strong!')

generated = ''.join(random.choice(uppercase + lowercase + digits + specialCharacters) for _ in range(length))
print(generated)
