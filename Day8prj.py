alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def caesar(plain_text, numb_shift, direction_):
    cyper_txt = ""
    if direction_ == "decode" :
        numb_shift *= -1
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + numb_shift
            new_letter = alphabet[new_position]
            cyper_txt += new_letter
        else:
            cyper_txt += char

    print(f"Your {direction_} message is '{cyper_txt}' ")

restart = True
while restart :
    
    direction = input("Type encode to encrypt, and decode to decrypt \n").lower()
    text  = input("Type your message: ").lower()
    shift = int(input("Number of shift: "))
    shift = shift % 26
    caesar(plain_text=text, numb_shift=shift, direction_=direction)
    reset = input("Do you want to encode or decode, yes or no").lower()
    if reset == "no":
        restart = False
        print("Thank you for using caesar")
      
    


