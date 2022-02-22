#!/usr/bin/env python
# coding: utf-8

# In[11]:


A = [[0,2,4,9,50],[0,0,3,54,53],[0,0,0,10,52],[0,0,0,0,51],[0,0,0,0,0]]


def minimum_metro(A):
    '''This code will take a matrix of all possible paths from one point to the other, 
    and will give a path which connects them all at minimum cost.'''
    
    # code to make elements lower triangle elements non zero if triangular matrix
    for i in range(len(A)):
        for j in range(len(A[i])):
            if i>j:
                A[i][j] = A[j][i]
                
    result = []
    fincost = []
    final = []
    cost = []
    i = 0
    for j in range(len(A[i])):
        # Appends the first row of the matrix, to ensure we go to all the metro stations (0,1,2,3,4...)
        if i == j:
            A[i][j] = 10000000000  #to get [0,0] into our cost array to compare with costs which are lesser.
        if j>=i:
            result.append([i,j])
            cost.append(A[i][j])
            
    # Here we compare the first row values with other elements going to that point to get minimum value
    
    for p in range(len(result)):
        j = p
        for i in range(len(A)):
            if i!=j: 
#                 print("i,j,p,cost,cost[p],A[i][j]:",i,j,p,cost,cost[p],A[i][j])
                if cost[p] > A[i][j]:
                    result.remove(result[p])
                    result.insert(p,[i,j])
                    cost.remove(cost[p])
                    cost.insert(p,A[i][j])
    #Lastly we remove the loops from our code
    
#     for i in range(len(result)):
#         result[i] = result[i].sort()
#         if count(result[i])>1:
#             result.remove(result[i])
#             cost.remove(cost[i])

# My code doesn't take care of loops, I believe we'd require a complex algorithm for that?

    return result, sum(cost)    

print(minimum_metro(A))


# In[7]:


from igraph import *

result, cost = minimum_metro(A)
g = Graph()
g.add_vertices(n = len(A))
g.add_edges(minimum_metro(A)[0])
layout = g.layout("kk")
plot(g, layout=layout)


# In[9]:


import random

def create_a_matrix(n):
    A = []
    for i in range(n):
        A.append([0]*n)
        for j in range(n):
            if i<j:
                A[i][j] = A[i][j] + random.randint(1,50)
    return A

K = create_a_matrix(5)
print(minimum_metro(K))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




