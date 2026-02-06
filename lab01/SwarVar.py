import re

def varSwap(inputTuple: tuple) -> tuple:
    '''Swapping two tuple values'''
    return (inputTuple[1], inputTuple[0])

def tupleProcessing(inputString: str) -> tuple:
    '''convert string input to tuple'''
    pattern = r"([0-9.]+)"
    value = re.findall(pattern, inputString)
    return tuple(map(float, value))

def main():
    '''Main function'''
    inputString = input()
    resultTuple = tupleProcessing(inputString)
    print(varSwap(resultTuple))

if __name__ == "__main__":
    main()
