n=int(input())
a={}
for i in range(n):
    str=input()
    if str in a:
        a[str]=a[str]+1
    else:
        a[str]=1
for i in a.values():
    print(i,end=' ')

