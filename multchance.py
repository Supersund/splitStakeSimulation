otherStakes = [0.05 for i in range(10)]
ourStakes = [0.05 for i in range(10)]

Er = 4 # This is a variable that can be manipulated

for i in range(len(otherStakes)):
    otherStakes[i] /= Er

for i in range(len(ourStakes)):
    ourStakes[i] /= Er

otherStakesZeroWinChance = 1
for i in otherStakes:
    otherStakesZeroWinChance *= (1-i)

ourStakesZeroWinChance = 1
for i in ourStakes:
    ourStakesZeroWinChance *= (1-i)

ourStakesOneWinChance = 0

for currStake in ourStakes:
    newStakes = ourStakes.copy()
    newStakes.remove(currStake)
    currValue = currStake
    for stake in newStakes:
        currValue *= (1-stake)
    ourStakesOneWinChance += currValue

moreThanOneWinnerChance = (1-ourStakesZeroWinChance-ourStakesOneWinChance)*otherStakesZeroWinChance
print(moreThanOneWinnerChance)