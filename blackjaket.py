import random

def start_game():
    def draw_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card_draw = random.choice(cards)
        return card_draw


    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2 :
            return 0
        
        if 11 in cards and sum(cards) > 21 :
            cards.remove(11)
            cards.append(1)
    
        return sum(cards) 
    
    user_card = []
    computer_card = []

    for _ in range(2):
        user_card.append(draw_card())
        computer_card.append(draw_card())

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw"
        elif user_score == 0:
            return "You Win"
        elif user_score > 21:
            return "You Lose"
        elif computer_score > 21:
            return "You Win"
        elif computer_score == 0:
            return "You Lose"
        elif user_score > computer_score:
                print("You Win")
        elif computer_score > user_score:
                print("You Lose")



    game_over = False
    while not game_over:
        user_score = calculate_score(user_card) 
        computer_score = calculate_score(computer_card)
        print(f"Your card is {user_card}, current score {user_score}")
        print(f"Computer first card is {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
            
        else: 
            is_continue = input("Do you want to draw another card yes or no ")
            if is_continue == 'yes':
                user_card.append(draw_card())
                
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17 :
        computer_card.append(draw_card())
        
        computer_score = calculate_score(computer_card)

    print(f"Your final hand is {user_card}, current score {user_score}")
    print(f"Computer final hand is {computer_card}, current score {computer_score}")
    print(compare(user_score, computer_score))


    
   
while input("Type 'y' to start the game. ") == 'y':
  start_game()

