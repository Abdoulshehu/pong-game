import random


def score(user_guess, guess, turns):
           
    if user_guess > guess:
        print("Too Low")
        return turns -1
       
        
    elif user_guess < guess:
        print("Too High")
        return turns -1
    else:
        print(f"You got it!! the Answer is {guess} ")
        


def difficulty_level():
    select_level = input("Select Level 'Easy' or 'Hard'_ ").lower()
    if select_level == "hard":
        return 5
       
    else:
        return 10
     
def game():     
    print("Welcome to the number guess Game")
    print("I am thinking of number between 1 - 100")
    guess = random.randint(1, 101)


    turns =  difficulty_level()
    
    user_guess = 0
    while user_guess != guess:
        print(f"You Have {turns} attempts remaining")
        
        user_guess = int(input("Make a guess_ "))   
        turns =  score(guess, user_guess, turns)
        if turns == 0:
            print("you run out of attempt You Lose!")
            return
        elif user_guess != guess:
            print("Guess Again")
game()
while input("Play Again? yes or no ") == "yes":
    game()