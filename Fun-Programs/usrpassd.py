# Authentication Program
import os
import datetime

print('''Welcome to the Authentication System\nPlz enter your credentials''')
username = input('Username: ' )
passwd = input('Password: ')

if username == 'john' and passwd == 'john':
    print('Logged in as {}'.format(username))
elif username == 'sam' and passwd == 'sam':
    print('Logged in as {}'.format(username))
else:
    print('Login Failed')

