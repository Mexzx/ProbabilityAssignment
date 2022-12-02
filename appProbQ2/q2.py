import random
import math
import matplotlib.pyplot as plt

NUMBEROFSIMS=10000
NUMBEROFCARDS=100

def fillUpCards():
    deck=[0]*NUMBEROFCARDS
    for i in range(NUMBEROFCARDS):
        deck[i]=i+1
    return deck
def variance(results):
    varianceSum=0
    average=sum(results)/len(results)
    for i in range(len(results)):
        varianceSum+=math.pow(results[i]-average,2)
    return varianceSum/len(results)
results=[]
ogDeck=[]
averages=[]
variances=[]

for i in range(NUMBEROFSIMS):
    counter=0
    deck=[0]*NUMBEROFCARDS
    deck=fillUpCards()
    random.shuffle(deck)

    for j in range(len(deck)):
        if((deck[j]-1)==j):
            counter+=1

    results.append(counter)
    averages.append(sum(results)/len(results))
    variances.append(variance(results))
ogDeck=fillUpCards()
x=[]
for i in range(NUMBEROFSIMS)    :
    x.append(i+1)

                   
print("\naverage {0}".format(sum(results)/len(results)))
print("variance: {0}".format(variance(results)))
plt.plot(x,averages)
plt.xlabel("number of simulations")
plt.ylabel("average")
plt.title("How the average changes over the simulations")
plt.savefig('plotQ2A.png', dpi=300, bbox_inches='tight')

plt.show()

plt.plot(x,variances)
plt.xlabel("number of simulations") 
plt.ylabel("variance")
plt.title("How the variance changes over the simulations")
plt.savefig('plotQ2B.png', dpi=300, bbox_inches='tight')

plt.show()
