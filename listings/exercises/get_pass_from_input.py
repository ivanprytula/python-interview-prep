from getpass import getpass

username = input('Username: ')
# password = input('Password: ')  # not what we want actually...
password = getpass('Password: ')

print('Logging in...')
