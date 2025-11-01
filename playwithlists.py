a=[1,3,4,5,9,10]
ctr=0
for i in a:
    ctr+=i

print(ctr)
average=ctr/len(a)
print("sum = ", ctr)
print("average = ", average)
a.sort()
print("Smallest element is:", a[0])
print("largest element is:", a[-1])



