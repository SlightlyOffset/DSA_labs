"""Calculator V2 Optimized"""

def main():
    '''main'''
    n = int(input())
    
    if n == 1:
        print(1)
        return

    length = len(str(n))
    total_digits = 0

    # 1. Count digits for full ranges (e.g., 1-9, 10-99...)
    # 1-9 has 9 numbers of 1 digit
    # 10-99 has 90 numbers of 2 digits
    for i in range(1, length):
        total_digits += 9 * (10**(i-1)) * i

    # 2. Count digits for the remaining partial range
    # e.g., if n=105, we count 100 to 105
    remaining_count = n - 10**(length-1) + 1
    total_digits += remaining_count * length

    # 3. Add 'n' for the operators (matching your original logic)
    print(total_digits + n)

if __name__ == "__main__":
    main()