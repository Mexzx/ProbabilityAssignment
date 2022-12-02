import random
import math

NUMBEROFSIMS=100000
NUMBEROFCARDS=100

def fillUpCards():
    deck=[0]*100
    for i in range(NUMBEROFCARDS):
        deck[i]=i
    return deck
def variance(results):
    varianceSum=0
    for i in range(len(results)):
        varianceSum+=math.pow(results[i]-(sum(results)/len(results)),2)
    return varianceSum/len(results)
results=[]

for i in range(NUMBEROFSIMS):
    counter=0
    deck=[0]*NUMBEROFSIMS
    deck=fillUpCards()
    random.shuffle(deck)
    
    for j in range(NUMBEROFCARDS):
        if(deck[j]==j):
            counter+=1
    
    results.append(counter)
print("average {0}".format(sum(results)/len(results)))
print("variance: {0}".format(variance(results)))

