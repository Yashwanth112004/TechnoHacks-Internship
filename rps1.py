import random
count=0
count1=0
print("Rock-Paper-Scissors Game")
print("Let's Start the Game")
def game():
    global count,count1
    l=input("What's your Choice (Rock/Paper/Scissors): ").lower()
    a=["rock","paper","scissors"]
    b=random.choice(a)
    print("My Choice is: ",b)
    
    if((l.lower()=='rock' and b.lower()=='scissors') or (l.lower()=='paper' and b.lower()=='rock') or 
       (l.lower()=='scissors' and b.lower()=='paper')):
        print("CONGRATULATIONS! YOU ARE THE WINNER")
        count=count+1
        print("Your Score is: ",count)
        print("My Score is: ",count1)
    
    elif((l.lower()==b.lower())):
        print("IT'S A TIE MATCH")
        print("Your Score is: ",count)
        print("My Score is: ",count1)

    else:
        print("I AM THE WINNER")
        count1=count1+1
        print("Your Score is: ",count)
        print("My Score is: ",count1)
game()
m=input("DO YOU WANT TO PLAY AGAIN(yes/no): ").lower()=='yes'

while m:
    game()
    m = input("DO YOU WANT TO PLAY AGAIN (yes/no): ").lower() == 'yes'

    