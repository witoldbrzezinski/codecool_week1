import random
import string

print("Welcome in password generator")

length = int(input("How many characters should password has?"))

string_with_all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
password = ""
for i in range(0,length):
    password += random.choice(string_with_all_characters)    

print("Your password is: "+password)