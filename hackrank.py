# import numpy as np
# N= int(input())

# A = [list(map(int, input().split())) for i in range(N)]
# B = [list(map(int, input().split())) for i in range(N)]

# print(np.matmul(A, B))

def avg(a):
    total = sum (a)
    print(total)
    average = (total /len(a))
    return average
a=list(map(int,input( ).split()))   
print(avg(a))