import random, string
length = int(input('Please enter the length you would like your password to be: '))

while length > 50:
    print('This length incorrect')
    length = int(input('Please enter the length you would like your password to be: '))

while length < 0:
    print('This length is too short')
    length = int(input('Please enter the length you would like your password to be: '))

generated = ''.join(random.choice(string.ascii_letters) for _ in range(length))
print(generated)