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



