number=input("Enter a number: ")
largest_digit=0
for numbers in number:
    numbers=int(numbers)
    if numbers>largest_digit:
        largest_digit=numbers
        
print(f"The largest digit is {largest_digit}")