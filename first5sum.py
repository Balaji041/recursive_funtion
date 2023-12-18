def largestsum(lis):
    l=sorted(lis,reverse=True)
    print(sum(l[:5]))
lis=list(map(int,input().split(",")))
largestsum(lis)

"""
input:12,1,22,6,14,7
61
"""
