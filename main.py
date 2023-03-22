# an encoder/decoder with a shift of 3

# by moxi and lyn

def encoder(password):
    res = ""
    for char in password:
        res += str(int(char) + 3)
    return res

# moxi's decoder
def decoder(password):
    # initialise variables
    decoded_message = ''

    # adjust and add each character
    for character in password:
        decoded_message += str(int(character) - 3)

    # return result
    return decoded_message


if __name__ == "__main__":
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            raw = input("Please enter your password to encode: ")
            encoded = encoder(raw)
            print("Your password has been encoded and stored!")
        elif option == 2:
            decoded = decoder(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.")
        elif option == 3:
            break
