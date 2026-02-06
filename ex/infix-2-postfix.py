def infix_to_RPN(infix_exp: str) -> str:
    '''Convert infix expression to RPN'''
    prec = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    output = []
    stack = []

    for char in infix_exp:
        if char.isspace():
            continue

        if char.isalnum():  # char is operand
            output.append(char)
        elif char == "(":   # enter the group
            stack.append(char)
        elif char == ")":   # ex1t and print the entire group
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()     # pop "("
        else:   # operator
            while stack and stack[-1] != "(" and prec.get(char, 0) < prec.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return "".join(output)

def main():
    infix_exp = input().strip()
    print(infix_to_RPN(infix_exp))

if __name__ == "__main__":
    main()
