#Dictionary

Roll_No = {1: "Usman", 2: "Ali", 3: "Adil", 4: "Hussain", 5: "Abbas", 6: "uzair", 7: "ejaz", 8: "Hamza", 9: "Ahsan", 10: "Asad"}

print(Roll_No)

print(type(Roll_No))

print(Roll_No.get(5))

Roll_No = {1: "Usman", 2: "Ali", 3: "Adil", 4: "Hussain", 5: "Abbas", 6: "uzair", 7: "ejaz", 8: "Hamza", 9: "Ahsan", 10: "Asad"}

print(Roll_No[5],Roll_No[6])



### Class Assignment

Names = {1: "Usman", 2: "Ali", 3: "Adil", 4: "Hussain", 5: "Abbas", 6: "uzair", 7: "ejaz", 8: "Hamza", 9: "Ahsan", 10: "Asad"}

rollno = {"k1": "001", "k2": "002", "k3": "003", "k4": "004", "k5": "005", "k6": "006", "k7": "007", "k8": "008", "k9": "009" , "k10": "10"}

marks = {"m1": 21, "m2": 22, "m3": 23, "m4": 24, "m5": 44, "m6": 19, "m7": 28, "m8" : 21, "m9": 32, "m10": 10}

print(Names)

print(rollno["k5"],Names[5],marks["m5"])


##### Auto Input Dictionary OPTIONAL ASSIGNMENT

inputdict = {}

myvar = int(input("How many items? "))

for i in range(myvar):
    key = input("Enter key: ")
    value = input("Enter value: ")
    inputdict[key] = value

print("Your dictionary:", inputdict)




