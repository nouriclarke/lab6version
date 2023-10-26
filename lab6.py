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

def decode(encrypt_pass):
    decoded_pass = ''
    for char in encrypt_pass:
        decode_val = int(char) - 3
        if decode_val < 0:
            decode_dict = {-3:'7',-2:'8',-1:'9'}
            decode_val = decode_dict[decode_val]
        decoded_pass += str(decode_val)
    return decoded_pass


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
            decoded_pass = decode(encoded_pass)
            print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}')
        elif choice == "3":
            break
        else:
            print("Invalid option, please try again")
