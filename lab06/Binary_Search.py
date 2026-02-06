# %%
import json

# %%
class Student:
    def __init__(self, ID, name, GPA):
        self.__name = name
        self.__ID = ID
        self.__GPA = GPA

    def get_name(self):
        return self.__name
    def get_ID(self):
        return self.__ID
    def get_GPA(self):
        return self.__GPA

    def print_details(self):
        print(f"ID: {self.__ID}")
        print(f"Name: {self.__name}")
        print(f"GPA: {self.__GPA:.2f}")

# %%
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid].get_name()
        # Increment once per iteration (one "probe")
        comparisons += 1

        if mid_val == target:
            return arr[mid], comparisons, mid
        if mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return None, comparisons, -1

# %%
def main():
    std = json.loads(input().strip())
    students = [Student(s["id"], s["name"], s["gpa"]) for s in std]
    # Binary search requires the list to be sorted by the search key
    students.sort(key=lambda x: x.get_name())
    target = input().strip()
    result, comparisons, index = binary_search(students, target)
    if result:
        print(f"Found {target} at index {index}")
        result.print_details()
        print(f"Comparisons times: {comparisons}")
    else:
        print(f"{target} does not exists.")
        print(f"Comparisons times: {comparisons}")

# %%
if __name__ == "__main__":
    main()


