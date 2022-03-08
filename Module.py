a=[12,4,6,-2,0,9]
result=[]
final=[]
for i in range(0,len(a)):
    for j in range(0,len(a)):
        result.append(a[i]-a[j])

for i in result:
    if result[i]>0:
        final.append(result[i])


final.sort()
print(final[0])



        

