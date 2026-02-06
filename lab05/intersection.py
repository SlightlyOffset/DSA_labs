"""Check for intersection between three list"""
import json

def is_intersect(s1: set, s2: set, s3:set) -> bool:
    '''Check for intersection'''
    return bool(s1 & s2 & s3)


def main():
    '''main'''
    ls1 = json.loads(input())
    ls2 = json.loads(input())
    ls3 = json.loads(input())
    print(is_intersect(set(ls1), set(ls2), set(ls3)))

if __name__ == "__main__":
    main()
