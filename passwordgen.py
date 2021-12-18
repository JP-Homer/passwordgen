import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,+-[]*~_#:?'
char_list = []
output = []

pass_length = int(input('Enter the length of the password: '))
omitted = input("Enter any special characters that are not allowed '.,+-[]*~_#:?': ")
pass_num = int(input('Enter the amount of passwords to create: '))

for char in chars:
    char_list.append(char)

for num in range(len(omitted)):
    char_list.remove(omitted[num])

for i in range(pass_num):
    pw = ''
    for num in range(pass_length):
        pw += random.choice(char_list)
    print(pw)
