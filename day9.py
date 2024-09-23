


def secret_bid(bidders):
    heighest_bid = 0
    winner = ""
    for bidder in bidders:
        highest = bidders[bidder]
        if highest > heighest_bid:
            heighest_bid = highest
            winner = bidder 
    print(f"{winner} is the winner with highest bid of ${heighest_bid}")

bid = {}
new_value = True
while new_value:
    name = input("Enter Name: ")
    price = int(input("What is your bid: $"))
    bid[name] = price
    bid_again = input("Is there any bidder, yes or no ? ")
    if bid_again == "no" :
        secret_bid(bidders=bid)
        new_value = False
        
  

     
  
    
    


# student_score = {
#     "Abdul" : "81",
#     "Musa" : "79",
#     "Shehu" : "99",
#     "Usman" : "78",
#     "Sani" : "64",
# }

# student_grade = {}
# for score in student_score:
#     name = student_score[score]
#     if name >= "91":
#         student_grade[score] = "Outstanding"
#     elif name >= "81":
#        student_grade[score] = "Excellent"
#     elif name >= "71":
#         student_grade[score]  = "Acceptable"
#     else:
#        student_grade[score] = "Failed"



# print(student_grade)



