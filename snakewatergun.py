import random
list=["snake",'water',"gun"]
counter=1
myscore=0
computerscore=0
while counter<=10:
    computerchoice=random.choice(list)
    print("yourchoice s for snake w for water g for gun")
    yourchoice=input()
    if yourchoice=="s" and computerchoice=="water":
        myscore=myscore+1
        counter=counter+1
    elif yourchoice=="s" and computerchoice=="gun":
        computerscore=computerscore+1
        counter=counter+1
    elif yourchoice=="w" and computerchoice=="gun":
        myscore=myscore+1
        counter=counter+1
    elif yourchoice=="w" and computerchoice=="snake":
        computerscore=computerscore+1
        counter=counter+1
    elif yourchoice=="g" and computerchoice=="snake":
        myscore=myscore+1
        counter=counter+1
    elif yourchoice=="g" and computerchoice=="water":
        computerscore=computerscore+1
        counter=counter+1
    elif yourchoice=="s" and computerchoice=="snake":
        counter=counter+1
    elif yourchoice=="w" and computerchoice=="water":
        counter=counter+1
    elif yourchoice=="g" and computerchoice=="gun":
        counter=counter+1
    else:
        print("please give correct input")
        continue
if computerscore>myscore:
    print("computer won")
elif myscore>computerscore:
    print("you won")
elif myscore==computerscore:
    print("its a tie")