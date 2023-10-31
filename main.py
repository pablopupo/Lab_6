def encode(password):
    encoded_password = ""
    for digit in password:
        new_digit = (int(digit) + 3) % 10
        encoded_password += str(new_digit)
    return encoded_password


def decode(password):
    decoded_password = ""
    for char in password:
        dec_pass = (int(char) - 3) % 10
        decoded_password += str(dec_pass)
    return decoded_password


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        user_input = input("Please enter an option:")

        if user_input == '1':
            password = input("Please enter a password to encode: ")
            encoded_pass = encode(password)
            print(f"The encoded password is: {encoded_pass}")
        elif user_input == '2':
            if 'encoded_pass' in locals():
                decoded_pass = decode(encoded_pass)
                print(f"The decoded password is: {decoded_pass}")
            else:
                print("You need to encode a password first.")
        elif user_input == '3':
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
