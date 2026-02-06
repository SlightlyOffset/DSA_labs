'''Fabonacci series using recursion with cache memorization'''

import functools

@functools.lru_cache(maxsize=None)
def fabonacci_lru(n):
    '''fabonacci function'''
    if n <= 0:
        return 0
    elif n == 1:
        return n
    return fabonacci_lru(n-1) + fabonacci_lru(n-2)

def main():
    '''main function'''
    num = int(input())
    print(fabonacci_lru(num))

if __name__ == "__main__":
    main()
