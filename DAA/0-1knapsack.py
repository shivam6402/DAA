def solve_knapsack(val,wt,W):
    n=len(val)-1

    def knapsack(W, n):
        if n<0 or W<=0:
            return 0
        
        if wt[n]>W:
            return knapsack(W, n-1)
        else:
            return max(val[n]+ knapsack(W - wt[n], n-1), knapsack(W ,n-1))
        
    return knapsack(W,n)

if __name__=="__main__":
    val=[]
    wt=[]
    n=int(input("Enter the number of items: "))
    print("Enter the profit and weight of each items: ")
    for i in range(n):
        val_i=int(input("Value of item: ".format(i+1)))
        wt_i=int(input("Weight of item: ".format(i+1)))
        val.append(val_i)
        wt.append(wt_i)

    W=int(input("Enter the knapsack weight of capacity: "))
    max_value=solve_knapsack(val,wt,W)
    print("Maximum Value: ", max_value)

