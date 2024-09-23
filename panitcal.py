import math

def paint_calculator(height, width, cover ):
    cans = math.ceil(height * width / cover)
    print(f"You need {cans} cans of paint")

    
   

#h_test = int(input("Height "))
#w_test = int(input("Width "))
coverage = 5
#paint_calculator(height=h_test, width=w_test, cover=coverage)    


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's  a prime number")
    else:
        print("It's not a prime number")

n = int(input("Check this number:- "))
prime_checker(number = n)