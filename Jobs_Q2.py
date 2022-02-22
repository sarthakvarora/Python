import random

arr_k = []
kz = 2
for i in range(200):
    arr_k.append(kz)
    kz = round(kz+0.10,2)

def job_offer(simuls,offers):

    # This snippet creates 'simuls' lists with each simulation having 'offers' job offers ranging from 0 to 35 LPA.
    all = []
    for i in range(simuls):
        L = []
        for j in range(offers):
            L.append(random.randint(0,35))
        all.append(L)
    
    # Now we want to check for each array the best offer, and store it's index
    
    print(arr_k)
    print(maxes2)
    print(len(maxes2))
    max2 = maxes2[0]
    indeks2 = 0
    for z in range(1,len(maxes2)):
        if maxes2[z]>max2:
            max2 = maxes2[z]
            indeks2 = z
    return arr_k[indeks2] 

print(job_offer(50,150))    