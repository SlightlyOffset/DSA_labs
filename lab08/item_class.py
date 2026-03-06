"""Item Class template"""


class Item:
    def __init__(self, name: str, price: float, weight: float):
        self.__name = name
        self.__price = price
        self.__weight = weight

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def weight(self) -> float:
        return self.__weight

    def get_cost(self) -> float:
        # Return price-to-weight ratio; infinite cost if weight is zero to avoid division by zero
        return self.__price / self.__weight if self.__weight > 0 else float("inf")

    def __str__(self) -> str:
        return f"{self.__name}\n{self.__price}\n{self.__weight}"


def main():
    import json

    # Parse item attributes from JSON input and construct an Item object
    item_in = json.loads(input())
    item = Item(item_in["name"], item_in["price"], item_in["weight"])
    print(item)

main()
