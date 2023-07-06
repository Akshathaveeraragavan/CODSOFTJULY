#This is a simple CALCULATOR which performs all the basic operations
name=input('Welcome user , Enter your name to get started ')
print("So , this is a simple calculator which can be used to perform the basic operations between multiple numbers")
print('REFER TO THE OPERATIONS AND THEIR CORRESPONDING NUMBERS\nADDITION-1\nSUBTRACTION-2\nMULTIPLICATION-3\nDIVSION-4\nFLOOR DIVISION-5\nFIND SQUARE ROOT-6\nFIND REMAINDER-7')
while 1:
    choice=int(input('Choose a number to perform the operation'))
    if choice==1:
        n1=eval(input("Enter num1"))
        n2=eval(input("Enter num2"))
        print(n1,'+',n2,'=',n1+n2)
    elif choice==2:
        n1=eval(input("Enter num1"))
        n2=eval(input("Enter num2"))
        print(n1,'-',n2,'=',n1-n2)
    elif choice==3:
        n1=eval(input("Enter num1"))
        n2=eval(input("Enter num2"))
        print(n1,'*',n2,'=',n1*n2)
    elif choice==4:
        n1=eval(input("Enter num1"))
        n2=eval(input("Enter num2"))
        print(n1,'/',n2,'=',n1/n2)
    elif choice==5:
        n1=eval(input("Enter num1"))
        n2=eval(input("Enter num2"))
        print(n1,'//',n2,'=',n1//n2)
    elif choice==6:
        n1=eval(input("Enter num2"))
        print(n1,'**','1/2 =',n1**(1/2))
    elif choice==7:
        n1=eval(input("Enter num1"))
        n2=eval(input("Enter num2"))
        print(n1,'%',n2,'=',n1%n2)
    else:
        print('Invalid choice , please try again')
        continue
    ask=input("Do you want to perform one more operation: Y/N")
    if ask=='Y' or ask=='y':
        continue
    else:
        print('Thanks for using our calculator',name)
        break

    
