'''Stack (Create Stack)'''

class ArrayStack:
    '''
    An array containing data
    '''
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data) -> None:
        """pushStack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self) -> str:
        """popStack"""
        try:
            if not self.data:
                raise IndexError
        except IndexError:
            print("Underflow: Cannot pop data from an empty list")
            return "None"
        self.size -= 1
        return self.data.pop()

    def is_empty(self) -> bool:
        """isEmpty"""
        return self.size == 0

    def get_stack_top(self) -> str:
        """getStackTop"""
        if not self.data:
            print("Underflow: Cannot get stack top from an empty list")
            return "None"
        return self.data[-1]

    def get_size(self) -> int:
        """getSize"""
        return self.size

    def print_stack(self) -> None:
        """printStack"""
        print(self.data)

def is_parentheses_matching(expression: str) -> bool:
    '''Parentheses Checker'''
    stack = ArrayStack()
    matched = True

    for char in expression:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            top = stack.pop()

            if top == "None":
                matched = False
                continue

            if (char == ')' and top != '(') or \
               (char == ']' and top != '[') or \
               (char == '}' and top != '{'):
                return False

    return stack.is_empty() and matched

def main():
    '''main function'''
    expression = input()
    if is_parentheses_matching(expression):
        print(f"Parentheses in {expression} are matched")
        print("True")
    else:
        print(f"Parentheses in {expression} are unmatched")
        print("False")

if __name__ == "__main__":
    main()
