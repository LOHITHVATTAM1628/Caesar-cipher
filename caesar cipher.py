alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key):
    chipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_popsition=(position+shift_key)%26
            chipher_text=chipher_text+alphabet[new_popsition]
        else:
             chipher_text=chipher_text+char
    print(chipher_text)
def decryption(chipher_text,shift_key):
    plain_text=""
    for char in chipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_popsition=(position-shift_key)%26
            plain_text=plain_text+alphabet[new_popsition]
        else:
             plain_text=plain_text+char
    print(plain_text) 
end=False 
while not end:                        
    what_to_do=input("type 'encrypt for encryption,type 'decrypt for decryption :\n")
    text=input("type your message :\n").lower()
    shift=int(input("enter shift key :\n"))
    if what_to_do=='encrypt':
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=='decrypt':
        decryption(text,shift)    
    play_again=input("play again type 'yes' or exit 'no' :")
    if play_again =='no':
        end=True
        print("Have a nice day ! bye")
