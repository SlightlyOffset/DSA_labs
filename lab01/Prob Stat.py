score = []
bestOfThree = 0

for _ in range(4):
    score.append(int(input()))

for _ in range(3):
    highest = max(score)
    bestOfThree += score.pop(score.index(highest))

print(bestOfThree)