import random
import matplotlib.pyplot as plt


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
averages=[]

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
    averages.append(sum(results)/len(results))
sumOfResults=sumFunc(results)
print("Rolls needed: ")
for i in range(len(results)):
    print("{0}, ".format(results[i]),end="")
print("\nExpected number of dice rolls: {0}\n".format(sumOfResults/len(results)))
x=[0]*NUMBEROFSIMULATION
for i in range(len(x)):
    x[i]=i
plt.plot(x,averages)
plt.xlabel("number of simulation")
plt.ylabel("average")
plt.title("change of average over the number of simulations")
plt.savefig('plot2.png', dpi=300, bbox_inches='tight')
plt.show()
