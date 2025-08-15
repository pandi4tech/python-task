# import module 
import random

# get the integer input of password length
passlen = int(input("Enter the length of password:"))

# password letters ,numbers and symbols
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#*"

# join the random password to given length of the characters
p =  "".join(random.sample(s,passlen ))

# print the password
print (p)

