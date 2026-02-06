def copyStack(stack1: list, stack2: list):
    while stack2:
        stack2.pop()

    if not stack2 and stack1:
        for x in stack1:
            stack2.append(x)

    return stack2

s1 = [10, 20, 30, 40]
s2 = [55, 35]
s2 = copyStack(s1, s2)
print(s1)
print(s2)
