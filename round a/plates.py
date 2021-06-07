
def getInput():
    return list(map(int, input().split()))
    
def pickPlates(N, stacks, P, K):
    
    #edge case if Dr.Patel can take every single plate
    if(P == (N * K)):
        return sum(sum(x) if isinstance(x, list) else x for x in stacks)

    tab = [[0] * (P + 1)]* K 

    for i in range(1, N):
        for j in range(P):
            for x in range(0, min(j, K)):
                tab[i][j] = max(tab[i][j], i + x +  tab[i - 1 ][j - x] ) 
                
    return tab

        
    

#input
n_cases = int(input(""))
for case in range(n_cases):
    n_stacks, size, n_plates = map(int, input().split())
    stacks = []
    for i in range(n_stacks):
        stacks.append(getInput())
    #output for each case
    print(f"Case #{case + 1}: {    pickPlates(n_stacks, stacks, n_plates, size)}")

    
