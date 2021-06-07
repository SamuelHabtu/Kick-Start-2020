def getInput():
    
    return list(map(int, input().split()))
    
def nPurchasable(houses, budget):
    
    bought = 0
    for house in houses:
        if(house <= budget):
            bought += 1
            budget -= house
        else:
            return bought
    return bought


n_cases = int(input(""))
for case in range(n_cases):
    n_houses, budget = getInput()
    houses = getInput()
    houses.sort()
    print(f"Case #{case + 1}: {nPurchasable(houses, budget)}")

