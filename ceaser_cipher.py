alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            ]


def ceaser_cipher(original_text, shift_amount, direction):
    if direction == "decrypt":
        shift_amount *= -1
    cipher_text = ""

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            cipher_text += alphabet[shifted_position]

        else:
            cipher_text += letter

    print(f"your ceaser_cipher text is {cipher_text}")


game_is_on = True
while game_is_on:
    text = input("Type your message:\n").lower()
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("invalid direction , please enter again")
        continue
    shift = int(input("Type your shift number:\n")) % 26

    ceaser_cipher(text, shift, direction)

    still_game = input("Do you still want the game? type (y/n)")
    if still_game != "y":
        game_is_on = False
        print("Good Bye")
