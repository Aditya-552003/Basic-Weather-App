import random
import string as st
char=""
len=int(input("enter size of password: "))
letters=input("include letters?(y/n): ")
numbers=input("include numbers?(y/n): ")
symbols=input("include symbols?(y/n): ")
if letters=="y":
    char+=st.ascii_letters
if letters=="y":
    char+=st.digits
if letters=="y":
    char+=st.punctuation
password="".join(random.choices(char,k=len))
print("your password is: ",password)