# ---------------------------------------------------------------------------- #
#                                     Day_4                                    #
# ---------------------------------------------------------------------------- #

from num2words import num2words

num = int(input("Enter any number: "))
word = num2words(num)
print(f"Output :{word.capitalize()}")



# output 
# Enter any number: 123
# Output :One hundred and twenty-three

# Enter any number: 345
# Output :Three hundred and forty-five

