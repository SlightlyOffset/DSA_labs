'''Stedent Grouping'''

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

def main():
    '''main function'''
    num_groups = int(input())
    num_students = int(input())

    # Generate a dictionary of unique each stack
    stacks = [ArrayStack() for _ in range(num_groups)]
    # temporary placeholder for students
    students = [input() for _ in range(num_students)]

    stack_pointer = 0   # pointer for grouping
    for student in students[::-1]:
        stacks[stack_pointer].push(student)
        stack_pointer += 1
        if stack_pointer == num_groups:
            stack_pointer = 0

    # output
    for stack in stacks:
        member_str = ""
        for name in stack.data:
            member_str += name + ", "
        print(f"Group {stacks.index(stack) + 1}: {member_str[:-2]}")
if __name__ == "__main__":
    main()
