def employee(name,age,salary,city):
    print("Name :",name)
    print("Age :",age)
    print("Salary :",salary)
    print("City :",city)

def main():
    # Positional
    employee("Aryan",21,2000.5,"Malkapur") # correct
    print("-"*20)
    employee(26,"Aryan","Malkapur",2000.5) # wrong
    print("-"*20)
    # Keyword
    employee(age=26,name="Aryan",city="Malkapur",salary=2000.5) # Correct
  

if __name__ == ("__main__"):
    main()

