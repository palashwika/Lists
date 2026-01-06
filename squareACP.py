numlist=int(input("Enter the lowest value for a range: "))
numlist2=int(input("Enter the highest value for a range:"))
limit=range(numlist,numlist2+1)

squarelist=[]
for i in limit:
   square=i**2
   squarelist.append(square)
print("The square values are: ",squarelist) 

even=[]
odd=[]
for i in squarelist:
    if i%2==0:
       even.append(i)
    else:
       odd.append(i) 
print("The even numbers in this square value list are ", even)
print("The odd numbers in this square value list are ", odd)





    





            
