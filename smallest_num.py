def small(num):
    print(min(num))

nums=input().split(",")
num=[]
for i in nums:
    num+=[int(i)]
small(num)

"""
2,3,-1,5
-1
"""
