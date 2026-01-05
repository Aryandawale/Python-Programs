def Mutiplication (value1,value2):
    Ans = 0 # local variable
    Ans = value1*value2
    return Ans

def main():
    no1 = 0 
    no2 = 0
    result = 0

    #############################################

    no1 = int(input("Enter 1st number : "))
    no2 = int(input("Enter 2nd Number : "))

    result=Mutiplication(no1,no2)
    print("Multiplication is :", result)

main()
