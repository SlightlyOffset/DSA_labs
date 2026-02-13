import json
import re

_NATURAL_RE = re.compile('([0-9]+)')

def natural_key(text):
    '''Key function for natural alphanumeric sorting (e.g., 'A2' < 'A10').'''
    # Split text into list of strings and numbers, converting numbers to int for proper comparison
    return [int(c) if c.isdigit() else c.lower() for c in _NATURAL_RE.split(str(text))]

def insertionSort(arr, last, key=lambda x: x):
    '''Sorts a list in ascending order using the insertion sort algorithm.'''

    compareTimes = 0
    steps = []
    # Pre-calculate keys for efficiency
    keys = [key(x) for x in arr[:last+1]]

    for current in range(1, last + 1):
        item = arr[current]
        item_key = keys[current]
        walker = current - 1

        # Shift elements of the sorted segment that are greater than the item to the right
        while walker >= 0:
            compareTimes += 1
            if keys[walker] > item_key:
                arr[walker + 1] = arr[walker]
                keys[walker + 1] = keys[walker]
                walker -= 1
            else:
                break

        # Insert the item into its correct position
        arr[walker + 1] = item
        keys[walker + 1] = item_key
        steps.append(arr.copy())
    return steps, compareTimes

def selectionSort(arr, last, key=lambda x: x):
    '''Sorts a list in ascending order using the selection sort algorithm.'''

    compareTimes = 0
    step = []
    # Pre-calculate keys for efficiency
    keys = [key(x) for x in arr[:last+1]]

    for current in range(last):
        min_index = current
        # Find the minimum element in the unsorted portion of the array
        for walker in range(current + 1, last + 1):
            compareTimes += 1
            if keys[walker] < keys[min_index]:
                min_index = walker

        # Swap the found minimum element with the first element of the unsorted portion
        if min_index != current:
            arr[current], arr[min_index] = arr[min_index], arr[current]
            keys[current], keys[min_index] = keys[min_index], keys[current]
        step.append(arr.copy())
    return step, compareTimes

def bubbleSort(arr, last, key=lambda x: x):
    '''Sorts a list in ascending order using the bubble sort algorithm.'''

    compareTimes = 0
    step = []
    # Pre-calculate keys for efficiency
    keys = [key(x) for x in arr[:last+1]]

    for current in range(last + 1):
        swapped = False
        # Iterate backwards from the end to bubble the smallest element to the front
        for walker in range(last, current, -1):
            compareTimes += 1
            # Swap if the element is smaller than the previous element
            if keys[walker] < keys[walker - 1]:
                arr[walker], arr[walker - 1] = arr[walker - 1], arr[walker]
                keys[walker], keys[walker - 1] = keys[walker - 1], keys[walker]
                swapped = True
        step.append(arr.copy())
        # Optimization: If no swaps occurred, the list is already sorted
        if not swapped:
            break
    if not step:
        step.append(arr.copy())
    return step, compareTimes

def printResult(sortedList, compareTimes):
    # Print the state of the list at each step and the total comparisons
    print("\n".join(str(step) for step in sortedList))
    print(f"Comparison times: {compareTimes}")

def main():
    # Read input data and the last index to sort
    dataList = json.loads(input())
    lastIndex = int(input())

    # Perform bubble sort using the natural key
    sortedList, compareTimes = bubbleSort(dataList, lastIndex, key=natural_key)
    printResult(sortedList, compareTimes)

if __name__ == "__main__":
    main()
