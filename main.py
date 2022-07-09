from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(plain_text,shift_amount,cipher_direction):
    cipher_text = ""
    for letter in plain_text:
        if letter not in alphabet:
            new_letter = letter
        else:
            position = alphabet.index(letter)
            
            if cipher_direction.lower() == "encode": 
                new_position = position + shift_amount
            elif cipher_direction.lower() == "decode":
                new_position = position - shift_amount
            else:
                print("Please check input.")
                return
            
            while new_position > 25:
                new_position -= 26
                
            while new_position < 0:
                new_position += 26
            
            new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The {cipher_direction} text is '{cipher_text}'")

stop = False

while not stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = input("Type the shift number:\n")
    while not shift.isnumeric():
        print("You enter non-numeric value.")
        shift = input("Type the shift number:\n")
    shift = int(shift)
    text_list =list(text)
    caesar(plain_text=text,shift_amount=shift,cipher_direction=direction)
    stop_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if stop_input.lower() == 'yes':
        stop = False
    elif stop_input.lower() == 'no':
        stop = True
        print("Good Bye 😃")