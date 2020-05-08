evolved = 0
evolves = []
boxers = []
candies = []
n = int(input())


for i in range(n):
    boxers.append(input())
    candies.append([int(x) for x in input().split()])
    required = candies[i][0]
    available = candies[i][1]
    evolves.append(0)
    while(available >= required):
        evolves[i] += 1
        available = available - required + 2
        evolved += 1
print(evolved)
print(boxers[evolves.index(max(evolves))])
    