print("")

while True:
    name = input("Enter student name:")
    subject = input("Enter subject:")
    marks = int(input("Enter marks:"))

    result = ""
    if marks>100 or marks<0:
        print("!!Invalid marks!!")
        result = "Invalid"
    elif marks>=75:
        result = "Distiction"
    elif marks>=60:
        result = "Pass"
    else:
        result = "Fail"
    
    print("\n------------------------------")
    print(f"{name} - {subject} - {result}")
    print("------------------------------")


    bool1 = input("\nDo you want to enter another student?(y/n)-")
    print("------------------------------")
    if bool1 == "n":
        break

    
    