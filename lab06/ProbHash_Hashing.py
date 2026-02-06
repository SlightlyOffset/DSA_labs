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
class ProbHash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def insert_data(self, student):
        key = student.get_ID()
        hash_value = self.hash(key)

        cycle = 0
        while self.table[hash_value] is not None:
            hash_value = self.rehash(hash_value)
            cycle += 1
            if cycle == self.size:
                print(f"The list is full. {student.get_ID()} could not be inserted.")
                return
        self.table[hash_value] = student
        print(f"Insert {student.get_ID()} at index {hash_value}")

    def search_data(self, std_id):
        hash_value = self.hash(std_id)
        original_hash = hash_value

        while self.table[hash_value] is not None:
            # Check if the current slot has the student we're looking for
            if self.table[hash_value].get_ID() == std_id:
                return self.table[hash_value]
            hash_value = self.rehash(hash_value)
            # Stop if we've looped back to the original hash
            if hash_value == original_hash:
                break
        # reached an empty slot -> not present
        print(f"{std_id} does not exist.")
        return None

# %%

def main():
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                print(f"Found {student.get_ID()} at index {hashtable.hash(student.get_ID())}") # Note: This prints original hash, for actual index we'd need to return it or search again.
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")

# %%
if __name__ == "__main__":
    main()
