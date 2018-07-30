def get_weighted_mean(nums, weights):
    n1 = len(nums)
    n2 = len(weights)
    if n1!=n2:
        #print "List of numbers and weights are not of the same length!"
        return
    else:
        n=n1
    xw_sum = 0
    sum_of_w = 0
    for i in range(n):
        xw_sum += x[i]*w[i]
        sum_of_w += w[i]
    weighted_mean = round(xw_sum/sum_of_w,1)
    return weighted_mean

n = int(input())
x = [float(i) for i in input().split(' ')]
w = [float(i) for i in input().split(' ')]

ws = get_weighted_mean(x,w)
print(ws)