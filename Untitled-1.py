
print("Welcome to the tip Calculator")
total_bill = float(input("Insert the total amount?__ "))
percentage = int(input("Kindly Choose the 10%, 12% & 15% tip__  "))
t_per = total_bill * percentage/100
p_total = t_per + total_bill
num_pple = int(input("How many people to split the bill?__"))
total = p_total / num_pple
new_total = round(total, 2)

print(f"Total amount to be paid by person is {new_total} ")