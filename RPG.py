import string
import random
print("PASSWORD GENERATOR")
while(True):
    l=int(input("Enter Length of your Password: "))
    lt=input("Do the Password need Letters(y/n): ").lower()=='y'
    n=input("Do the Password need Numbers(y/n): ").lower()=='y'
    s=input("Do the Password need Symbols(y/n): ").lower()=='y'
    c=""
    if lt:
        c += string.ascii_letters
    if n:
        c += string.digits
    if s:
        c += string.punctuation
    password = ''.join(random.choice(c) for _ in range(l))
    print("Random Generated Password: ",password)
 