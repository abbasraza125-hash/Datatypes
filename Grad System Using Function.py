#Grad System Using Function

print("Welcome to the Grade System")

inputs = int(input("Enter your total marks: "))


def calculate_grade(Marks):

    # Grade A 

    if Marks >=  90:
        print("You have achieved Grade A")
           
    # Grade B
    elif Marks >= 80:
        print("You have achieved Grade B")
    
    # Grade C
    
    elif Marks >= 70:
        print("You have achieved Grade C")  

    # Grade D
    elif Marks >= 60:
        print("You have achieved Grade D")  

    else:
        print("You have achieved Grade F")  

calculate_grade(inputs)


