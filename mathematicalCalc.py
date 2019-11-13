myPr1 = 1-(1-(1/1000))**4
otherPr1 = 1-(1-(1/1000))**2

totalChance = 0
otherPrBetter = 0
for i in range(1,10000):
    otherPrBetter = 0
    myPrI = (1-myPr1)**(i-1)*myPr1
    for j in range(1,i+1):
        otherPrBetter += (1-otherPr1)**(j-1)*otherPr1
    totalChance += myPrI*(1-otherPrBetter)

for i in range(1,100):
    totalChance += ((1-myPr1)**(i-1)*myPr1*(1-otherPr1)**(i-1)*otherPr1)/2

print(totalChance)