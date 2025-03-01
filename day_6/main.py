# ---------------------------------------------------------------------------- #
#                                     Day_6                                    #
# ---------------------------------------------------------------------------- #


user_input = int(input("Enter a number: "))
binary = bin(user_input)[2:]
if binary == binary[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
