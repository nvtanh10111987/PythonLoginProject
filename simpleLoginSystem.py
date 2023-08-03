
# Variables
import os, random, string, time
path = "accounts.txt"


def login():
    
    # Get username
    print('LOGIN!\nPlease Enter your username and password')
    username = input("Username:")
    while len(username) == 0:
        username = input("Username:")

    # Get password
    password = input("Password:")
    while len(password) == 0:
        password = input("Password:")

    # Test for username and password
    
    with open(path) as line:
        lines = line.readlines()
        i = 0
        lineInFile = 0
        while i < len(lines):
            if username+' '+password+'\n' == lines[i]:
                i = len(lines)
                lineInFile = 1
            i+=1
        if lineInFile == 1:
            print('Logged In')
        else:
            option=input(('Please make sure username and password are correct. Try again! Or Create a new account!\n')+
            ('1. Try again\n2. Create a new account\n3. Back to main.\nPlease enter your choice: '))
            if option =='1':
                login()
            elif option == '2':
                register()
            elif option == '3':
                menu()
            else:
                stop()


def register():

    # Get username
    print('Register\nCreate a new account!')
    checkFile = True

    while checkFile == True:
        username = input("Username:")
        checkFile = False
        while len(username) == 0:
            username = input("Username:")

        with open(path) as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if username == lines[i].split()[0]:
                    checkFile = True
                    print('Username already taken! Try different one!')
                    break
                i+=1



    # Random password?
    defaultLength = 10
    if input('Generate random password? [y]/[n]'.lower()) == 'y':
        lettersOption = input('Use letters? [y]/[n]').lower()
        symbolsOption = input('Use symbols? [y]/[n]').lower()
        numbersOption = input('Use numbers? [y]/[n]').lower()
        length = input('Password length (leave blank for default(default length is 10 characters): ')
        autoPW = ''
        if lettersOption == 'y':
            autoPW += string.ascii_letters
        if numbersOption == 'y':
            autoPW += string.digits
        if symbolsOption == 'y':
            autoPW += '!@#$%^&*()'
        random.seed = (os.urandom(32))
        if length == '':
            length = defaultLength
        password = ''.join(random.choice(autoPW) for i in range(int(length)))
        print('Your password is', password)

    else:
        # Get password
        password = input("Password:")
        while len(password) == 0:
            password = input("Password:")
    print('Create account successful')

    # Write username and password to file
    with open(path, 'a') as file:
        file.write((username+' '+password+'\n'))
    
    menu()

    
def view():
    count =1
    for line in open("accounts.txt", "r").readlines():
        login_info = line.split()
        print(f'{count}.Username: {login_info[0]} \n    Password: {login_info[1]}')
        count+=1

    menu()


def stop():
    print('Exit')
    time.sleep(2)


def menu():
    print('MAIN MENU')
   
    userInput = input(' 1. Login\n 2. Register\n 3. View\n 4. Exit\n Choose the following options (1, 2, 3, 4):\n')
    if userInput == '1':
        login()
    elif userInput == '2':
        register()
    elif userInput == '3':
        view()
    elif userInput == '4':
        exit()
print('Choose the following options (1, 2, 3, 4):\n')

# MAIN
menu()
