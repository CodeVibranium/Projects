import string
import random

def create_password():
    s1=list(string.ascii_uppercase)
    s2=list(string.ascii_lowercase)
    s3=list(string.punctuation)
    s4=list(string.hexdigits)
    s5=s1+s2+s3+s4
    random.shuffle(s5)
    length_of_password=int(input("Enter the length of password : "))
    password=("".join(s5[0:length_of_password]))
    print(password)
create_password()
