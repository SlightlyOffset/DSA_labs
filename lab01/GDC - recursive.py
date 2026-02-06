'''finding GCD using recursion'''
def gdc(a: int, b: int) -> int:
    '''GCD function'''
    if not a:
        return b
    return gdc(b % a, a)

def main():
    '''main function'''
    num1 = int(input())
    num2 = int(input())
    print(gdc(num1, num2))

if __name__ == "__main__":
    main()
