"""Calculate coin changes using a greedy algorithm."""

def conExchange(amount, coins):
    """Calculate the change for a given amount using a greedy algorithm."""
    # Initialize the change dictionary with all coin denominations set to 0
    change = {}

    def _coinDictUpdate(data):
        for coin in data:
            if coin not in change:
                change[coin] = 0

    _coinDictUpdate(coins)

    for coin in sorted(coins.keys(), reverse=True):
        # Check if there are any coins available for exchange
        if sum(coins.values()) == 0:
            return change, False

        while amount >= coin and coins[coin] > 0:
            change[coin] = change.get(coin, 0) + 1
            amount -= coin
            coins[coin] -= 1
            # If the amount becomes 0, we can break out of the loop early
            if amount == 0:
                break

    # If there is still an amount left after trying to exchange with all coins, it means the coins are not enough
    if amount > 0:
        return change, False
    return change, True

def convert_key(data):
    """Convert the keys of a dictionary from strings to integers."""
    return {int(k): v for k, v in data.items()}

def main():
    """Main function."""
    import json
    payment = int(input())
    data = convert_key(json.loads(input()))
    change, enough = conExchange(payment, data)
    print(f"Amount: {payment}")

    if not enough:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")
        for coin, count in change.items():
            print(f"  {coin} baht = {count} coins")
        print(f"Number of coins: {sum(change.values())}")

if __name__ == '__main__':
    main()
