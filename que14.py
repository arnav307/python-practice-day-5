import random
guesses=0
for i in range(1,6):
    computer=random.randint(1,20)
    player=int(input("Enter a random number: "))
    if 1<=player<=20:
        if player>computer:
            print("To high")
            guesses+=1
        elif player<computer:
            print("To low")
            guesses+=1
        elif player==computer:
            print("Congratulation you have win!!!!!")
        else:
            print("please enter a number generating from 1 to 20.")
print(f"You have guess {guesses} guesses the correct answer is {computer}.")