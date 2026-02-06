def concatQueue(Q1: list, Q2: list):
    if Q2:
        for x in Q2:
            Q1.append(x)
    return Q1

Q1 = [10, 20 , 30, 40]
Q2 = [45, 25]
print(f"Added {Q2} to {Q1}")
print(f"Got {concatQueue(Q1, Q2)}")
