#THIS IS A SIMPLE QUIZ GAME TO BE PLAYED BY ENTERING ANSWERS TO THE QUESTIONS ASKED
count=0
name=input("Enter your name to get started!")
print("Welcome,",name)
print("RULES AND REGULATIONS:\n*You will be asked to answer a total of 10 questions.\n*All questions would be based on general knowledge only.")
print("*You will be awarded 1 mark if your answer is correct.\n*There is no negative marking in this quiz game.\nALL THE VERY BEST !!! ")
u=input('PRESS ENTER TO GET STARTED !') # pressing enter starts the game
while u=='':
    ans1=input(("1. Baby frog is known as?"))
    if ((ans1=="TADPOLE")or (ans1=="tadpole") or (ans1=='Tadpole')):
        print("Gud.Your right.A baby frog is termed as a tadpole.")
        count=count+1
    else:
        print("Hm.Tats a wrong answer.A baby frog is termed as a tadpole.")
    ans2=input(("2. Name the national flower of India?"))
    if ((ans2=="LOTUS")or (ans2=="lotus") or (ans2=='Lotus')):
            print("Gud.Your right.The national flower of India is lotus flower.")
            count=count+1
    else:
        print("Hm.Tats a wrong answer.The national flower of India is lotus flower.")
    ans3=input(("3. Name the biggest continent in the world?"))
    if ((ans3=="ASIA")or (ans3=="asia") or (ans3=='Asia')):
        print("Gud.Your right.The largest continent in the world is Asia.")
        count=count+1
    else:
        print("Hm.Tats a wrong answer.The largest continent in the world is Asia.")
    ans4=input(("4. Which colour symbolises peace?"))
    if ((ans4=="WHITE")or (ans4=="white") or (ans4=='White')):
        print("Gud.Your right.The colour of peace is White.")
        count=count+1
    else:
        print("Hm.Tats a wrong answer.The colour of peace is White.")
    ans5=input(("5. Name the largest mammal?"))
    if ((ans5=="BLUE WHALE")or (ans5=="blue whale") or (ans5=='Blue Whale') or (ans5=='Blue whale ')):
        print("Gud.Your right.The largest mammal found on earth is Blue whale.")
        count=count+1
    else:
        print("Hm.Tats a wrong answer.The largest mammal found on earth is Blue whale.")
    ans6=input(("6. Name the place known as the Roof of the World?"))
    if ((ans6=="TIBET")or (ans6=="tibet") or (ans6=='Tibet')):
        print("Gud.Your right.Tibet is named as the Roof of the world.")
        count=count+1
    else:
        print("Hm.Tats a wrong answer.Tibet is named as the Roof of the world.")
    ans7=input(("7. Which is the principal source of energy for the Earth?"))
    if ((ans7=="SUN")or (ans7=="sun") or (ans7=='Sun')):
        print("Gud.Your right.The principal source of energy for Earth is Sun.")
        count=count+1
    else:
        print("Hm.Tats a wrong answer.The principal source of energy for Earth is Sun.")
    ans8=input(("8. Name a bird that lays the largest eggs?"))
    if ((ans8=="OSTRICH")or (ans8=="ostrich") or (ans8=='Ostrich')):
        print("Gud.Your right.The bird that lays the largest eggs are the Ostrich.")
        count=count+1
    else:
        print("Hm.Tats a wrong answer.The bird that lays the largest eggs are the Ostrich.")
    ans9=input(("9. Name the National Heritage Animal of India?"))
    if ((ans9=="ELEPHANT")or (ans9=="elephant") or (ans9=='Elephant')):
        print("Gud.Your right.Elephant is named as the National Heritage of India.")
        count=count+1
    else:
        print("Hm.Tats a wrong answer.Elephant is named as the National Heritage of India")
    ans10=input(("10. Name the planet known as the Red Planet?"))
    if ((ans10=="MARS")or (ans10=="mars") or (ans10=='Mars')):
        print("Gud.Your right.Mars is named as the Red planet.")
        count=count+1
    else:
        print("Hm.Tats a wrong answer.Mars is named as the Red planet.")
    print("CONGRATS.YOU SCORED",count,"OUT OF 10")
    if count<3:
        print("OOH..That wasn't a great score. You need to improve",name)
    elif count<6:
        print("Not bad..You can improve much more",name)
    else:
        print("That's a great score",name)
    o=input('Would you like to play again? Y/N')
    if o=='Y' or o=='y':
        continue
    else:
        print('Hope you enjoyed the game!!!\nThanks for playing!\nPlease come again!')
        break
else:
    print('Alright! Come back once you are ready!!!')
    print('Bye',name)


