"""SommationV1 BIG(O)"""
def formula_method(n:int) -> int:
    '''find the sommation from 1 to n using proper formula'''
    return int(n*(n+1)/2)

def main():
    '''main'''
    print(formula_method(int(input())))

if __name__ == "__main__":
    main()
