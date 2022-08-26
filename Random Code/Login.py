print('=== System is online. ===')
status = 0

def mainMenu():
    print(f'''
Welcome to Prototype Program!

login status = {status}

1. Login
2. Register Data
''')
    inputUser = input('>>> ')
    if inputUser == '1':
        login()
    elif inputUser == '2':
        registerData()
    else:
        print('Invalid Option!')
        mainMenu()

def registerData():
    print('Masukkan data : (COMING SOON)')
    mainMenu()

def login():
    global status
    username = (input('Username : '))
    password = (input('Password : '))
    if (username == "admin") and (password == "admin"):
        status += 1
        print('Welcome, Admin!')
        mainMenu()
    else:
        print('Invalid Username or Password.')
        return login()

mainMenu()
print(status)
print('=== System is offline. ===')