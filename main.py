from addition import Addition
from multiplication import Multiplication


while True:
    print("Enter the number 01 :  ")
    num1 = int(input())
    print("Enter the number 02 :  ")
    num2 = int(input())
    print("Addition       -->  1")
    print("Multiplication -->  2")
    print("Exit           -->  3")
    choice = int(input("Choice please :-->  "))

    if(choice == 1):
        result = Addition.add(num1,num2)
    
    elif(choice == 2):
        result = Multiplication.multiply(num1,num2)
    
    elif(choice == 3):
        break

    else:
        result = "Enter a valid input"
    
    print(result)


    
