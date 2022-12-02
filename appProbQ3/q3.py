import random
import matplotlib.pyplot as plt

STARTINGMONEY=20
NUMBEROFSIMS=10000

wins=0
endIn10=0
winArray=[]
gameUnder10=[]
winsAverageLength=[]
LoseAverageLength=[]
aveWin=[]
aweL=[]
for i in range(NUMBEROFSIMS):
    tempMoney=STARTINGMONEY
    counter=1

    while(tempMoney>0 and tempMoney<100):
        headOrTail=random.randint(0,1)
        if(headOrTail==0):
            tempMoney+=10
        else:
            tempMoney-=10
        counter+=1
    if(tempMoney==100):
        wins+=1
        winsAverageLength.append(counter)
        aveWin.append(sum(winsAverageLength)/len(winsAverageLength))
    if(tempMoney==0):
        LoseAverageLength.append(counter)
        aweL.append(sum(LoseAverageLength)/len(LoseAverageLength))

    if(counter<=10):
        endIn10+=1
    
    winArray.append(wins/(i+1))
    gameUnder10.append(endIn10/(i+1))


print("1. The probability you win the game: {0} \n".format((wins)/NUMBEROFSIMS))
print("2. The probability the game ends within ten coin flips: {0}\n".format((endIn10/NUMBEROFSIMS)))
x=[]
for i in range(len(winsAverageLength)):
    x.append(i+1)

loosesaverage=[]
for i in range(len(aveWin)):
    loosesaverage.append(aweL[i])
plt.plot(x,aveWin,label="wins")  
plt.plot(x,loosesaverage,label="losses")  

plt.xlabel("number of simulations") 
plt.ylabel("Rounds needed until the game ends average")
plt.title("Wins and losses game lengths average")
plt.legend()
plt.savefig('plotQ34.png', dpi=300, bbox_inches='tight')

plt.show()
print(sum(loosesaverage)/len(loosesaverage))
print(sum(aveWin)/len(aveWin))
