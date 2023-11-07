import timeit

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        if weight == 0:
            self.value_per_unit = 0
        else:
            self.value_per_unit = value / weight

def fractional_knapsack(items, capacity):
    # Sort items by value per unit in descending order
    items.sort(key=lambda x: x.value_per_unit, reverse=True)
    
    total_value = 0
    selected_items = []

    for item in items:
        if capacity >= item.weight:
            # Add the whole item to the knapsack
            total_value += item.value
            selected_items.append(item)
            capacity -= item.weight
        else:
            # Add a fraction of the item to the knapsack
            fraction = capacity / item.weight
            total_value += fraction * item.value
            selected_items.append(Item(item.weight * fraction, item.value * fraction))
            break

    return total_value, selected_items

def main():
    items = []
    num_items = int(input("Enter the number of items: "))
    
    for i in range(num_items):
        weight, value = map(int, input(f"Enter weight and value for item {i + 1} (separated by space): ").split())
        items.append(Item(weight, value))

    capacity = int(input("Enter the capacity of the knapsack: "))

    total_value, selected_items = fractional_knapsack(items, capacity)
    total_time = timeit.timeit(lambda: fractional_knapsack(items, capacity), number=1000)

    print("Selected items:")
    for item in selected_items:
        print(f"Weight: {item.weight}, Value: {item.value}")

    print("Total value in the knapsack:", total_value)
    print("Total time: ",total_time)

if __name__ == "__main__":
    main()

# weights = 1 3 5 4 1 3 2
# values = 5 10 15 7 8 9 4
# capacity = 15