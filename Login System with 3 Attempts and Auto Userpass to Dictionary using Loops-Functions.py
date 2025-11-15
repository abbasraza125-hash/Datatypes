
# Login System with 3 Attempts and Auto User/pass to Dictionary using Functions

def set_user_pass():
    print("Please Set your Username and password")
    inputdict = {}
    my = int(input("How many Users? "))
    for i in range(my):
        key = input("Enter Student Username: ")
        value = input("Enter Student Password: ")
        inputdict[key] = value
    return inputdict

print("Please Set your Username and password")

inputdict = {}

my = int(input("How many Users? "))

for i in range(my):
    key = input("Enter Student Username: ")
    value = input("Enter Student Password: ")
    inputdict[key] = value

print("Now Login")

username = input("Enter your username: ")
if username in inputdict:
    attempts = 3
    for attempt in range(attempts):
        passwd = input("Enter your password: ")
        if passwd == inputdict[username]:
            print("Login Successful")
            break
        else:
            print("Login Failed")
else:
    print("Username not found")


print("Final Users Database:")
print(inputdict)    