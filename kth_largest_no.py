list_=list(map(int,input().split(",")))
soredt=sorted(list_,reverse=True)
second=int(input())
print(soredt[second-1])

"""
2,3,-1,5
2
output:3
"""
