password = ' '
while password != 'secret':
    password = input ('please enter the password: ')
    if password == 'secret':
        print('Wellcome: ')
    else:
        print('Sorry, the password you enterd is incorrect. Please try again.')