def encode(num):
    result = ""
    num = str(num)
    for i in num: # go through all i in string num
        i = int(i)+3 # convert i to integer and add 3 to encode
        result = result + str(i)
    return result

def decode (num):
    result = ""
    num = str(num)
    for i in num: # go through all i in string num
        i = int(i)-3 # convert i to integer and subtract 3 to decode
        result = result + str(i)
    return result


if __name__ == "__main__":
    menu_option = 1
    
    while menu_option != 3:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        menu_option = int(input("\nPlease enter an option: "))
        if menu_option == 1:
            num = input("Please enter your password to encode: ")
            encoded = encode(num) # encodes the input
            print ("Your password has been encoded and stored!\n")
        elif menu_option == 2:
            # print the result
            print ("The encoded password is " + str(encoded) + ", and the original password is " + str(num) + ".\n")

