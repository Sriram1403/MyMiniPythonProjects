import random
import string
from time import sleep

# input the length ofthe password
Length = int(input('Enter the length of the password : '))
print("wait a Second! Generating Your Password!")
sleep(1)
# Define The Data
Lower = string.ascii_lowercase
Upper = string.ascii_uppercase
Number = string.digits

# Combine the data
all = Lower + Upper + Number

# use random
temp = random.sample(all,Length)

# create the random
password = "".join(temp)

print("Your Password Is : "+password)
