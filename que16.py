import random
guesses=0
win=0
while True:
    player=int(input("Enter a dice: "))
    computer=random.randint(1,6)
    if 1<=player<=6:
        
        if player>computer:
            guesses+=1
        elif player<computer:
            guesses+=1
        elif player==computer:
            win+=1
            print("congratulation!!! You enter a correct number from dice!!!")
    else:
        print("please enter a number from 1 to 6")
    q=input("would you like to q or c: ")
    if q=='q':
        break
print(f"You have guess {guesses} times.")
print(f"You have win {win} times")