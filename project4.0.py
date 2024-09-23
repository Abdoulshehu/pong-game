import random

random_ans = random.randint(0, 1)
if random_ans == 1 :
    print("Head")
else:
    print("Tail")


list_of_name =  input("insert the list of names separated by ','\n")
name_list = list_of_name.split(" ,")

picked_person = random.choice(list_of_name)
print(picked_person + " is paying for the meal.")