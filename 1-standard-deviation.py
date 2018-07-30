n = int(input())
x = [int(i) for i in input().split(' ')]

sum = 0
for i in range(n):
    sum += x[i]
    
mean = int(sum/n)
#print(mean)

sum_of_sqd = 0
for i in x:
    sum_of_sqd += (i-mean)**2
#print(sum_of_sqd) 

stddev = round((sum_of_sqd/n)**0.5,1)

print(stddev)
