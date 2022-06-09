import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(start_text, shift_amount, cipher_direction):
    end_text = ""
    encrypt_or_decrypt = ""
    over_shift = shift_amount % 25
    if direction == "encode":
        encrypt_or_decrypt = "encrypted"
    elif direction == "decode":
        encrypt_or_decrypt = "decrypted"
    if shift_amount > 25:
        shift_amount = over_shift
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {encrypt_or_decrypt} message is: {end_text}")


print(art.logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(text, shift, direction)

    restart = input("\nWould you like to restart the cipher program?\nPress y or n\n")
    if restart == "n":
        should_end = True
        print("Goodbye.")
