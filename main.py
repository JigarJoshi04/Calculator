from addition import Addition
from multiplication import Multiplication
from division import Division

from integerdivision import IntegerDivision
=======
from modulo import Modulo


while True:
    print("Enter the number 01 :  ")
    num1 = int(input())
    print("Enter the number 02 :  ")
    num2 = int(input())
    print("Addition       -->  1")
    print("Multiplication -->  2")
    print("Division       -->  3")
    print("Integer Division->  4")

    print("Modulo         -->  5")
    print("Exit           -->  6")
    choice = int(input("Choice please :-->  "))

    if(choice == 1):
        result = Addition.add(num1,num2)
    
    elif(choice == 2):
        result = Multiplication.multiply(num1,num2)
    
    elif(choice == 3):
        result = Division.division(num1,num2)

    elif(choice == 4):

        result = IntegerDivision.integerdivision(num1,num2)

    elif(choice == 5):
        

        result = Modulo.mod(num1, num2)
        break 

    elif(choice == 6):
        break
    
    else:
        result = "Enter a valid input"
    
    print(result)


    
