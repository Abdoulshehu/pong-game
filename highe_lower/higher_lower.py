from data1 import *
import random
print(logo)


score = 0
start_game = int(input("1.Start Game\nQ.Quit Game\n-->"))
# Choose a ramdom celebrity
is_correct = True
while is_correct:
    celeb1= random.choice(data)
    celeb2 = random.choice(data)
    if celeb1 == celeb2:
        celeb2 = random.choice(data)

    print(f"Current Score: {score}")
# extracting  the name country and description from dictionary
    def format_data(celeb):
        name = celeb["name"]
        description = celeb["description"]
        country = celeb["country"]
        return f": {name} a {description} from {country}"
        

   
   
    if start_game == 1:
        print(f"A: {format_data(celeb=celeb1)}")
        print(vs)
        print(f"B: {format_data(celeb=celeb2)}")


        def compare_followers(A, B, answer):
            if A > B :
                return answer == "A"
            else:
                return answer  == "B"             

        answer = input("Who has more followers on instagram? A or B ").upper()

        A = celeb1["follower_count"]
        B = celeb2["follower_count"]
        winner = compare_followers(A, B, answer)


        if winner:
            score += 1
            print("Correct!")

        elif answer == "Q":
             is_correct = False

        else:
            print(f"Wrong!")

    
    
   


  

 

      
