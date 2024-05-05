import random
import string

print("How long do you want your password to be")
length= int(input())
u= int(input("How many uppercase letters do you want"))
l= int(input("How many lowercase letters do you want"))
n= int(input("How many numbers letters do you want"))
s= int(input("How many special characters do you want"))



def characters(u,l,n,s):
    upperlen= u
    lowerlen= l
    numberlen= n
    speciallen= s

    upper=""
    lower=""
    number=""
    special=""


    for i in range(upperlen):
        upper = upper + random.choice(string.ascii_lowercase)
    for j in range(lowerlen):
        lower=lower + random.choice(string.ascii_uppercase)
    for k in range(numberlen):
        number= number + str(random.randint(0,9))
    for q in range(speciallen):
        special = special + str(random.choice(string.punctuation))

    return upper + lower + number + special 
       
       
    
        

password = characters(u,l,n,s)
print(password)