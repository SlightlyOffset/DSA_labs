'''Stack (Create Stack)'''

class ArrayStack:
    '''
    An array containing data
    '''
    def __init__(self, size=0, data=None):
        self.size = size
        if data is None:
            self.data = []
        else:
            self.data = data

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
        if not self.data:
            print("Underflow: Cannot pop data from an empty list")
            return "None"
        self.size -= 1
        return self.data.pop()

    def is_empty(self):
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

STACK_ = ArrayStack()

STACK_.push("100")
STACK_.push(100)
STACK_.push("3.14")
STACK_.push(3.14)
STACK_.push("66.4a")
STACK_.push("Ackerman")

STACK_.print_stack()

print(STACK_.get_size())
VAR1_ = STACK_.pop()
print(VAR1_)
STACK_.print_stack()
print(STACK_.get_size())

while not STACK_.is_empty():
    print(STACK_.pop())

print()
print(STACK_.pop())
print(STACK_.get_stack_top())
print(VAR1_)