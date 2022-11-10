x =str(input())
count =-1
list=[]
for a in x :
    count+=1
    list.append(a)
print(list)
for b in list:
    c = b * 2**int(count)
    count-=1
    print(c)
