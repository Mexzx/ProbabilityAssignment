import random

import matplotlib.pyplot as plt
NUMBEROFSIMULATION=10000
MAXNUMBERINDICE=12

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

results=[]
averages=[]

for i in range(NUMBEROFSIMULATION):
    quit=False
    temp=[False]*MAXNUMBERINDICE
    counter=0
    while(not quit):
        counter+=1
        randomNumber=random.randint(1,MAXNUMBERINDICE)
        temp[randomNumber-1]=True
        if(checkAllTrue(temp)):
            quit=True
    
    results.append(counter)
    x=sumFunc(results)
    averages.append(x/len(results))

    sum=0
    for i in range(len(results)):
        sum+=results[i]


print("average {0}".format(sum/len(results)))
x=[0]*NUMBEROFSIMULATION
for i in range(len(x)):
    x[i]=i
plt.plot(x,averages)
plt.xlabel("number of simulation")
plt.ylabel("average")
plt.title("change of average over the number of simulations")
plt.savefig('plot.png', dpi=300, bbox_inches='tight')

plt.show()


