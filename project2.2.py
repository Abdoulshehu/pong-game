print("WELCOME TO PIZZA JUNGLE :)")
print("Please do place your order!")
print("L for large $90")
print("M for medium $70")
print(" S for small $40")

order = input("Input size here_ ")
if order == "L" :
    total_bill = 90 
    print(f"bill: ${total_bill}")
    pepperoni = input("Doy want to add pepperoni? Y or N ")

    if pepperoni == "Y":
        total_bill += 10
        cheese = input("Do you want extra cheese Y or N ")
        if cheese == "Y" :
            total_bill += 5
            print(f"Your total bill is ${total_bill}")
        elif cheese == "N":
            print(f"your total bill is ${total_bill} and you will receive it shortly ")    
        else:
            print("Please enter the correct input!")
    elif pepperoni == "N":
        print(f"your total bill is ${total_bill}...")    
        cheese = input("Do you want extra cheese Y or N ")
        if cheese == "Y" :
            total_bill += 5
            print(f"Your total bill is ${total_bill}")
        elif cheese == "N":
            print(f"your total bill is ${total_bill} and you will receive it shortly ")    
        else:
            print("Please enter the correct input!")

    else:
        print("Please enter the correct input!")

elif order == "M" :
    total_bill = 70 
    print(f"bill: ${total_bill}")
    pepperoni = input("Doy want to add pepperoni? Y or N ")

    if pepperoni == "Y":
        total_bill += 10
        print(f"Your total bill is ${total_bill}")
        cheese = input("Do you want extra cheese Y or N")
        if cheese == "Y" :
            total_bill += 5
            print(f"Your total bill is ${total_bill}")
        elif cheese == "N":
            print(f"your total bill is ${total_bill} and you will receive it shortly ")    
        else:
            print("Please enter the correct input!")
    elif pepperoni == "N":
        print(f"your total bill is ${total_bill}... ")    
        cheese = input("Do you want extra cheese Y or N ")
        if cheese == "Y" :
            total_bill += 5
            print(f"Your total bill is ${total_bill}")
        elif cheese == "N":
            print(f"your total bill is ${total_bill} and you will receive it shortly ")    
        else:
            print("Please enter the correct input!")

    else:
        print("Please enter the correct input!")

elif order == "S":
    total_bill = 40 
    print(f"bill: ${total_bill}")
    pepperoni = input("Doy want to add pepperoni? Y or N ")
    if pepperoni == "Y":
        total_bill += 10
        print(f"Your total bill is ${total_bill}")
        cheese = input("Do you want extra cheese Y or N ")
        if cheese == "Y" :
            total_bill += 5
            print(f"Your total bill is ${total_bill}")
        elif cheese == "N":
            print(f"your total bill is ${total_bill} and you will receive it shortly ")    
        else:
            print("Please enter the correct input!")

    elif pepperoni == "N":
        print(f"your total bill is ${total_bill}...")    
        cheese = input("Do you want extra cheese Y or N ")
        if cheese == "Y" :
            total_bill += 5
            print(f"Your total bill is ${total_bill}")
        elif cheese == "N":
            print(f"your total bill is ${total_bill} and you will receive it shortly ")    
        else:
            print("Please enter the correct input!")

    else:
        print("Please enter the correct input!")

else:
    print("Please do choose L, M or S from the menu!")



