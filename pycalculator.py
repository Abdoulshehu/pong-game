print(f'''

             
            -----------------------------
            |                           |
            -----------------------------   -------
            |  1         2           3  |   |   +  |

            |  4         5           6  |   |  -   |

            |  7         8           9  |   |  *   |

            | .          0           =  |   |  /   |           
            -----------------------------   --------



''')












def calculator(value1, value2, operator_):
    if operator_ == "+":
        return value1 + value2
    elif operator_ == "-":
        return value1 - value2
    elif operator_ == "*":
        return value1 * value2 
    elif operator_ == "/":
        return value1 / value2
    else:
        print("Choose valid operator")
    








def reset():
    input1 = int(input("choose number "))
    operator = input("choose operator ")
    input2 = int(input("choose number "))
    answer = calculator(value1=input1, value2=input2, operator_=operator)
    print(f"{input1} {operator} {input2} = {answer}")
    is_true  = True
    while is_true:
        operator = input("choose operator ")
        input2 = int(input("choose number "))
        answer = calculator(answer, value2=input2, operator_=operator)
        print(f"{answer} {operator} {input2} = {answer}")
        restart = input("Start new calculation 'yes' or 'no' ")
        if restart == 'yes':
            reset()
        else:
             
             print(f" Your final answer is  {answer}")
             is_true = False


            


reset()