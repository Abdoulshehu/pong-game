import random





scissors = ('''
    ,______
___        )_______
            _______)
           _________)
         _____)
        _____)
        
''')

rock =  ('''
    ,______
___     ___)____
             ___)
           ____)
         _____)
        _____)
        
''')

paper =  ('''
    ,______
___        )_______
            _______)
           _________)
         ________)
        ______)
        
''')
choice = [scissors, paper, rock]
for_ans = input("Enter 'S', for scissor, 'P' for paper and 'R' for rock \n " ).upper()
if for_ans == "S" : 
    print(scissors) 
elif for_ans == "P" :
    print(paper)
elif for_ans == "R" :
    print(rock)
else:
    print("Wrong input.")

computer = random.choice(choice)

print(computer)

if computer == rock and for_ans == "P":
    print("You Win!!")
elif computer == rock and for_ans == "S" :
    print("You Lose!!!")
elif  computer == rock and for_ans == "R" :
    print("Draw!!")
elif  computer == paper and for_ans == "S" :
    print("You  Win!!")
elif  computer == paper and for_ans == "R" :
    print('You Lose!!!')
elif computer == paper and for_ans == "P" :
    print("Draw!!")

elif computer == scissors and for_ans == "P" :
     print("You Lose!!!")

elif computer == scissors and for_ans == "R" :
    print("You Win!!")

elif computer == scissors and for_ans == "S" :
    print("Draw!!")
else:
    pass



