# Accept : Multi parameters
# Return : Multi Value

def marvellous1(Value1,Value2,Value3):
    print("Inside Marvellous 1 :",Value1,Value2,Value3)
    return 11,21,51

def main ():
    Result1 = None
    Result2 = None
    Result3 = None
    Result1,Result2,Result3 = marvellous1("Python",21,"Aryan")
    print ("Return Value are  :", Result1,Result2,Result3)
    
if __name__ == "__main__":
    main()
