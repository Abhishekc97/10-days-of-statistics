#using the sort func from previous challenge
def sort(x):
    #temp = int()
    n = len(x)
    for j in range(1,n-1):
        for i in range(n-j):
            if x[i]>x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp
    return x

def find_median(array):
    length = len(array) 
    pivot = int(length//2)
    if (length%2) == 0:
        median = int( (array[pivot] + array[pivot-1]) / 2 )
    else:
        median = int(array[pivot])
    return median

def main():
    n = int(input())
    x = [int(i) for i in input().split(' ')]
    x_sorted = sort(x)
    #print(x_sorted)
    q2 = find_median(x_sorted)
    
    if (n%2) == 0:
        lower_half = x_sorted[0:(n//2)]
        upper_half = x_sorted[(n//2):]
    else:
        lower_half = x_sorted[0:(n//2)]
        upper_half = x_sorted[(n//2)+1:]
    
    q1 = find_median(lower_half)
    q3 = find_median(upper_half)
    print(q1)
    print(q2)
    print(q3)
if __name__ == '__main__':
    main()
    

