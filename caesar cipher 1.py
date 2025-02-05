alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Result: {cipher_text}")

end = False
while not end:
    what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Enter shift key:\n"))
    if what_to_do == 'decrypt':
        shift =shift*-1  
    encryption(text, shift)
    play_again = input("Play again? Type 'yes' to continue or 'no' to exit:\n").lower()
    if play_again == 'no':
        end = True
        print("Have a nice day! Bye!")
