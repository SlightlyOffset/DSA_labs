def infix_to_postfix(expression):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []
    
    for char in expression:
        if char.isalnum():  # Operand
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop '('
        else:  # Operator
            while stack and stack[-1] != '(' and prec.get(char, 0) <= prec.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())
    
    return "".join(output)

if __name__ == "__main__":
    expr = input("Enter infix expression (e.g., A+B*C): ")
    print("Postfix:", infix_to_postfix(expr))
