# if Else login system with User Define/set password

print("Please Set your username and password")
print("\n")

N = input("Enter your name: ")
P = input("Set your password: ")


print("\n") 

print("Please use your username and password to login\n")

username = input("Username: ")
password = input("Password: ")  

if username == N:
    if password == P:
        print("Login Successful")
    else:
        print("Incorrect Password") 

else:
    print("Please try again")       
