add=0
while True:
    num=int(input("Enter a number: "))
    if 100<=num<=200:
        if num%2==0:
            add+=num
        else:
            continue
    else:
        break
print(f"The sum of even num is {add}")