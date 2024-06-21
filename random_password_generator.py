'''
TASK 3  -   PASSWORD GENERATOR
Create a program that generates a random password of a user-defined length.
'''

import random
import string

nouns = ['employer','football','addition','analysis','baseball','customer','presence','guidance','proosal','hospital','strategy']
adjectives = ['determined','diligent','dynamic','entertaining','fair-minded','fantastic','fearless','friendly'	'funny'	'generous']

#simple password 
def weak_password():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    num = random.randrange(0,500)
    special_char = random.choice(string.punctuation)


    password = adjective[3:6] + noun[4:7] + str(num) + special_char
    return password


#strong password  
def strong_password():
    
    print("Enter the password length :")
    password_length = int(input())

    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$&*()"
    password = ""

    for i in range(password_length):
        password += random.choice(characters)

    return password

    

while True:

    print("Enter Type of Password you need :\n1.strong\n2.weak")
    if input()=="strong":
        password = strong_password()
    else:
        password = weak_password()

    print("The password is  :  %s"%password)

    #checking if user need other password
    print("Do you want more Stronger password ?")
    if not input()=="yes":
        break
    
print("\nThank you....!")