#THIS IS A SIMPLE PASSWORD GENERATOR
import random
list1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l',
'm','n','o','p','q','r','s','t','u','v'',w','x','y','z','!','@','#','$','%','^','&','*','(',')','?','{','}','~','+','=','_','-','1','2','3','4','5','6',
'7','8','9','0']
password=''
user=int(input('Hi user! Please enter the length of your password '))
for i in range(user):
    password+=random.choice(list1)
print('The Password generated for you is ',password)
    
