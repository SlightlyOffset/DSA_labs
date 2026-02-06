'''A simple rectangle'''

class Rectangle:
    '''
    A rectangle object with height and width

    :param height: height of the rectangle
    :type height: float
    :param width: width of the rectangle
    :type width: float
    '''
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self) -> float:
        '''
        Docstring for calculate_area

        :param self: N/A
        :return: area of the rectangle
        :rtype: float
        '''
        return self.height * self.width

    def calculate_perimeter(self) -> float:
        '''
        Docstring for calculate_perimeter

        :param self: N/A
        :return: perimeter of the rectangle
        :rtype: float
        '''
        return 2 * (self.height + self.width)

def main():
    '''main function'''
    height = float(input())
    width = float(input())

    rectangle = Rectangle(height, width)
    area = rectangle.calculate_area()
    perimeter = rectangle.calculate_perimeter()
    ops = input().lower().strip()

    if ops == "area":
        print(f"{area:.2f}")
    elif ops == "perimeter":
        print(f"{perimeter:.2f}")

if __name__ == "__main__":
    main()
