while True:
    num1=int(input("Enter a first number: "))
    num2=int(input("Enter a second number: "))
    operation=input("Would you like to add,sub,mul,div?: ")
    if operation=='add':
        add=num1+num2
        print(f"addition :",add)
    elif operation=='sub':
        sub=num1-num2
        print(f"subtraction:",sub)
    elif operation=='mul':
        mul=num1*num2
        print(f"multiply: ",mul)
    elif operation=='div':
        if num2==0:
            print("Error: Division by zero is not allowed.")
            continue
            div=num1/num2
            print(f"division: ",div)
    else:
        print("Invalid operation. Please choose add, sub, mul, or div.")
        continue 
    stop=input("Would you like to stop?: ")
    if stop=='q':
        break