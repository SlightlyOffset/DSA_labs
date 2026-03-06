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
        return f"{self.__name} -> {self.__weight} kg -> {self.__price} THB"

def knapsack(items, capacity):
    """Use greedy algorithm to pick the most valuable item first."""

    picked_items = []
    # Sort items by price-to-weight ratio descending to always pick the most valuable item first
    items.sort(key=lambda x: x.get_cost(), reverse=True)
    total_price = 0
    total_weight = 0
    for item in items:
        if total_weight + item.weight <= capacity:
            # Item fits within remaining capacity; add it to the knapsack
            total_price += item.price
            total_weight += item.weight
            picked_items.append(item)
        else:
            # Since items are sorted by cost, no subsequent item can improve the ratio; stop early
            break

    return picked_items, total_price

def main():
    import json

    items = []
    num_items = int(input())
    # Read each item from JSON input and build the items list
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in["name"], item_in["price"], item_in["weight"]))
        num_items = num_items - 1

    knapsack_capacity = float(input())
    picked_items, total_price = knapsack(items, knapsack_capacity)

    print(f"Knapsack Size: {knapsack_capacity} kg")
    print("===============================")
    for item in picked_items:
        print(item)
    print(f"Total: {total_price} THB")

main()
