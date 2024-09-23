import random
from words import word_list
from logo import logo

print(logo)
stages = ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
lives = 10
word_list 
choose_word = random.choice(word_list)


display = []
for letter in choose_word:
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    print(f"Current Live: {stages[lives]}")
    guess = input("Guess a letter: ").lower()
    if guess   in display:
        print(f"You have already guess '{guess}'")
    

    for position in range(len(choose_word)):
        letter = choose_word[position]
        #print(f"current position {position}\n current letter {letter}\n guessed letter {guess}")
        if letter == guess:
            display[position] = letter
            
    if guess not in choose_word:
        print(f"{guess} is not in the Guessing word!")
        lives -= 1
       
        if lives == 0:
            end_of_game = True
            print("You Lose!")
    print(f"{''.join(display)}")
    
      
    print(display)
    if "_" not in display:
        end_of_game = True
        print("YOU WIN!")


  