class Item:
    def __init__ (self,profit,weight):
        self.profit=profit
        self.weight=weight

def fractionalknapsack(w,arr):
    arr.sort(key=lambda x: x.profit/x.weight, reverse= True)
    finalValue=0.0
    for item in arr:
        if w>= item.weight:
            finalValue+=item.profit
            w-=item.weight

        else:
            finalValue += item.profit * (w/item.weight)
            break
    return finalValue

if __name__ =="__main__":
    n=int(input("Enter the number of items: "))
    arr=[]
    for i in range(n):
        profit=int(input("Enter the profit: "+str(i+1)+"-\n"))
        weight=int(input("Enter the weight: "+str(i+1)+"-\n"))
        arr.append(Item(profit,weight))

    w=int(input("Enter the weight of Knapsack: "))
    print("Maximum value: ",fractionalknapsack(w,arr))