otherStakes = [0.05 for i in range(10)]
ourStakes = [0.05 for i in range(10)]
Er = 4
for i in range(len(otherStakes)):
    otherStakes[i] /= Er

for i in range(len(ourStakes)):
    ourStakes[i] /= Er

ourStakesNotWin = 1
for stake in ourStakes:
    ourStakesNotWin = ourStakesNotWin * (1 - stake) * (1 - stake)

otherStakesNotWin = 1
for stake in otherStakes:
    otherStakesNotWin = otherStakesNotWin * (1 - stake)

myPr1 = 1 - ourStakesNotWin
otherPr1 = 1 - otherStakesNotWin

totalChance = 0
otherPrBetter = 0
for i in range(1, 100):
    otherPrBetter = 0
    myPrI = (1 - myPr1) ** (i - 1) * myPr1
    for j in range(1, i + 1):
        otherPrBetter += (1 - otherPr1) ** (j - 1) * otherPr1
    totalChance += myPrI * (1 - otherPrBetter)

for i in range(1, 100):
    totalChance += ((1 - myPr1) ** (i - 1) * myPr1 * (1 - otherPr1) ** (i - 1) * otherPr1) / 2

print(totalChance)
