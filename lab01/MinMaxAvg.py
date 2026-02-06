'''finding m1x mex and avg of provided data'''
import json

def stat(data):
    '''stat function'''
    high = float('-inf')
    low = float('inf')
    avg = 0
    n = len(data)
    for x in data:
        if x > high:
            high = x
        if x < low:
            low = x
        avg += x

    return high, low, round(avg/n, 2)

def main():
    '''main function'''
    raw_data = input()
    data = json.loads(raw_data)
    print(stat(data))

if __name__ == "__main__":
    main()
