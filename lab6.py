# Nouri Clarke
def encode(password):
    var = ''
    for i in password:
        result = int(i)
        result += 3
        if result >= 10:
            result %= 10
        var += str(result)
    return var


if __name__ == "__main__":
    while True:
        print("""
        Menu
        -------------
        1. Encode
        2. Decode
        3. Exit""")
        print()
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            encoded_pass = encode(password)
        elif choice == "2":
            pass
        elif choice == "3":
            break
        else:
            print("Invalid option, please try again")
