A = [1,1.5,4,0.5,7,5,3,4,1,6,3]

def housing_profits(A):
    '''Here we find the maximum profit in the housing market by buying in areas where the value is minimum and sell when it is increasingly highest.
    Inputs = Array of house prices on different days
    Outputs = Array of when to buy sell wait, and maximum profit.'''
    
    BSW = []
    
    # Here we mark all cases as Wait 'W'
    
    for j in range(len(A)):
        BSW.append('W')
        
    # Code to find areas where to buy and sell.
    # We take care of the corner cases and mark the leftover as buy or sell in case of min or max respectively.
        
    if A[0]<A[1]:
        BSW[0] = 'B'
    if A[-1]>A[-2]:
        BSW[-1] = 'S'
    for i in range(1,len(A)-1):
        if A[i]<A[i-1] and A[i]<A[i+1]:
            BSW[i] = 'B'
        elif A[i]>A[i-1] and A[i]>A[i+1]:
            BSW[i] = 'S'
            
    # Figuring out the profit in such a case
    #Here it is (4/1.5)*(7/0.5)*(4/3)*(18/1)
            
    for k in range(len(BSW)):
        if BSW[k] == 'B':
            indx = k
            val_B = A[k]
            break
    val = 1
    for p in range(indx+1,len(BSW)):
        if BSW[p] == 'B':
            val_B = A[p]
        if BSW[p] == 'S':
            val = A[p]*val/val_B
    
    return BSW, val

print(housing_profits(A))