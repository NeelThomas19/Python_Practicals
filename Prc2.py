K=int(input())
Room_list=list(map(int,input().split()))
n=len(Room_list)
temp_l=[]
Room_list.sort()
print(Room_list)
count=0
i=0
while(i<n):
    count=Room_list.count(Room_list[i])
    if(count==K):
        i=i+K
    else:
        print(Room_list[i])
        break

#1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2