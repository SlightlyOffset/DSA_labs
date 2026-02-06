"""SommationV1 BIG(O)"""
def loop_method(n:int) -> int:
    '''find the sommation from 1 to n using loop'''
    som = 0
    current = 1
    while current != n:
        som += current
        current += 1
    return som + current

def main():
    '''main'''
    print(loop_method(int(input())))

if __name__ == "__main__":
    main()
