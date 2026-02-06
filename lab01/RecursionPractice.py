import time

def explain_recursion():
    """
    Recursion is a programming technique where a function calls itself to solve a problem.
    It breaks a large problem into smaller, self-similar sub-problems.
    
    Every recursive function needs two things:
    1. Base Case: A condition that stops the recursion (e.g., if n == 0: return 1).
                  Without this, you get infinite recursion (Stack Overflow).
    2. Recursive Step: The part where the function calls itself with a modified argument
                       moving towards the base case.
    """
    print(explain_recursion.__doc__)

# --- Level 1: The Classic Example ---
def factorial(n):
    """
    Calculates n! (n * (n-1) * ... * 1) recursively.
    
    Example Trace for factorial(3):
    factorial(3) calls factorial(2)
        factorial(2) calls factorial(1)
            factorial(1) calls factorial(0)
                factorial(0) returns 1 (Base Case)
            factorial(1) returns 1 * 1 = 1
        factorial(2) returns 2 * 1 = 2
    factorial(3) returns 3 * 2 = 6
    """
    # 1. Base Case: 0! is defined as 1
    if n == 0:
        return 1
    
    # 2. Recursive Step: n! = n * (n-1)!
    else:
        result = n * factorial(n - 1)
        print(f"Returning {result} for factorial({n})") # Visualization
        return result

# --- Level 2: Multiple Recursive Calls ---
def fibonacci(n):
    """
    Returns the nth number in the Fibonacci sequence (0, 1, 1, 2, 3, 5, 8...).
    
    This demonstrates 'branching' recursion, where one call spawns multiple others.
    Warning: This is inefficient for large n without optimization (memoization),
    but excellent for understanding the concept.
    """
    # Base Cases
    if n <= 0: return 0
    if n == 1: return 1
    
    # Recursive Step
    return fibonacci(n - 1) + fibonacci(n - 2)

# --- Level 3: Processing Data Structures ---
def sum_nested_list(nested_list):
    """
    Calculates the sum of all numbers in a nested list of arbitrary depth.
    Input: [1, [2, 3], [4, [5]]]
    Output: 15
    """
    total = 0
    for element in nested_list:
        if isinstance(element, list):
            # Recursive Step: If it's a list, dive deeper!
            total += sum_nested_list(element)
        else:
            # Base logic: If it's a number, just add it.
            total += element
    return total

def main():
    print("--- 1. Understanding Factorial ---")
    print("Calculating factorial(5):")
    result = factorial(5)
    print(f"Result: {result}\n")

    print("--- 2. Fibonacci Sequence ---")
    n = 7
    print(f"Calculating Fibonacci({n}):")
    # A simple loop to show the sequence up to n
    seq = [fibonacci(i) for i in range(n+1)]
    print(f"Sequence: {seq}\n")

    print("--- 3. Challenge: Nested Lists ---")
    complex_data = [1, [2, 3], [4, [5, 6], 7], 8]
    print(f"Input List: {complex_data}")
    total = sum_nested_list(complex_data)
    print(f"Sum of all elements: {total}")

if __name__ == "__main__":
    main()