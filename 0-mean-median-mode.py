#import numpy as np
n = int(input())
x = [int(i) for i in input().split(' ')]
################################################################
#mean = np.mean(x)
sum = 0
for i in range(n):
    sum += x[i]
mean = float(sum/n)
print(mean)   
################################################################
#median= np.median(x)
pivot = int(n//2)
#x_sorted = np.sort(x)

def sort(x):
    #temp = int()
    for j in range(1,n-1):
        for i in range(n-j):
            if x[i]>x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp
    return x

x_sorted = sort(x)

#print(x_sorted)
#print(x_sorted[pivot])
#print(pivot)
median = float((x_sorted[pivot]+x_sorted[pivot-1])/2)
print(median)
################################################################

z = [(i, x_sorted.count(i)) for i in x_sorted]
z.sort(key=lambda z: z[1], reverse=True)    
mode = z[0][0]

print(mode)
