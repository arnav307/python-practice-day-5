string=input("Enter a string: ")
vowel='a','e','i','o','u'
vowel_count=0
for i in string:
    if i in vowel:
        vowel_count+=1
print(f"There are {vowel_count} in the string")
    
        