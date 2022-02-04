T=int(input())
Score_list=list(map(int,input().split()))
Score_list.sort()
mx=max(Score_list[0],Score_list[1])
secondmax=min(Score_list[0],Score_list[1])
n =len(Score_list)
for i in range(2,n):
    if Score_list[i]>mx:
        secondmax=mx
        mx=Score_list[i]
    elif Score_list[i]>secondmax and \
        mx != Score_list[i]:
        secondmax=Score_list[i]
 
print("Second highest number is : ",\
      str(secondmax))
