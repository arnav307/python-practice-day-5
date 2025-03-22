import random
round_played=0
win=0
while True:
    player=int(input("Enter a number: "))
    computer1=random.randint(1,6)
    computer2=random.randint(1,6)
    total_rolled=computer1+computer2
    round_played+=1
    
    if 2<=player<=12: 
        if total_rolled==player:
            print(f"congratulation you have won {computer1} + {computer2} = {total_rolled}")
            win+=1   
            win_percentage = (win / round_played) * 100
            print(f"You have played {round_played} round of game.")
            print(f"You have won {win} times and your percentage is {win_percentage}")
        else:
            print(f"You lost!!! the total is {total_rolled}")
    else:
        print("Please enter the number between 2 to 12")
    
    quit_continue=input("Would you like to stop(s) or continue(c): ")
    if quit_continue=='s':
        break


                
        