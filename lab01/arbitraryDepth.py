def sum_nested_list(nested_list: list) -> int:
    total = 0   # storing the total sum
    
    for element in nested_list:
        # if encounter a list inside. dive deeper into the list
        if isinstance(element, list):
            total += sum_nested_list(element)
        else:
            total += element
    return total

print("--- 3. Challenge: Nested Lists ---")
complex_data = [1, [2, 3], [4, [5, 6], 7], 8]
print(f"Input List: {complex_data}")
total = sum_nested_list(complex_data)
print(f"Sum of all elements: {total}")
