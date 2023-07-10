#This is a password generator using secret module
import secrets
import string 
letters=string.ascii_letters
numbers=string.digits
symbols=string.punctuation
result=letters+numbers+symbols
password=''
length=int(input("Hi user , Please enter the length of the password : "))
for i in range(length):
    password+=''.join(secrets.choice(result))
print('The generated password is:',password)
print('Hope this password helps!\nThanks for using our password generator!!!')

    
