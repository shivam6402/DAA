def solve_knapsack(val, wt, W):
    n = len(val) - 1

    def knapsack(W, n):
        # Base case
        if n < 0 or W <= 0:
            return 0

        # Higher weight than available
        if wt[n] > W:
            return knapsack(W, n - 1)
        else:
            return max(val[n] + knapsack(W - wt[n], n - 1), knapsack(W, n - 1))

    return knapsack(W, n)

if __name__ == "__main__":
    val = []
    wt = []
    
    n = int(input("Enter the number of items: "))
    
    print("Enter the values and weights for each item:")
    for i in range(n):
        val_i = int(input("Value of item {}: ".format(i + 1)))
        wt_i = int(input("Weight of item {}: ".format(i + 1)))
        val.append(val_i)
        wt.append(wt_i)

    W = int(input("Enter the knapsack weight capacity: "))

    max_value = solve_knapsack(val, wt, W)
    print("Maximum value:", max_value)