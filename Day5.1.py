student_height = input("Enter the Students height__ ").split()
for height in range(0, len(student_height)):
    student_height[height] = int(student_height[height])

highest_score = 0
for score in student_height:
    if score > highest_score:
        highest_score = score
print(f"The highest height is {highest_score}") 

total_height = 0
for heights in student_height:
    total_height += heights
total = total_height

num_height = 0
for student in student_height:
    num_height += 1
total_student = num_height
average = round(total /total_student )

print(f"The average students height is {average}")

