import random

def checkAllTrue(input):
    for i in range(len(input)):
        if(input[i]==False):
            return False
    return True
def sumFunc(input):
    x=0
    for i in range(len(input)):
        x+=input[i]
    return x

NUMBEROFSIMULATION=10000
MAXNUMBERINDICE=6
NUMBEROFDIFFERENTSUMS=11

results=[]

for i in range(NUMBEROFSIMULATION):
    quit=False
    temp=[False]*NUMBEROFDIFFERENTSUMS
    counter=0
    while(not quit):
        counter+=1
        dice1=random.randint(1,MAXNUMBERINDICE)
        dice2=random.randint(1,MAXNUMBERINDICE)
        sumOfDice=dice1+dice2
        temp[sumOfDice-2]=True
        if(checkAllTrue(temp)):
            quit=True
    results.append(counter)
sumOfResults=sumFunc(results)
print("Expected number of dice rolls: {0}\n".format(sumOfResults/len(results)))
