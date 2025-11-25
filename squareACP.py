num=input("Enter two numbers for a range with space in between ")
num_list=num.split()


if len(num_list)==2:
    start=int(num_list[0])
    stop=int(num_list[1])

    square=[]
    sq=[]
    odd=[]  
    even=[] 
    for i in range(start,stop+1):
        square=i**2 #begins storing values
        sq.append(square) #appends values wtihout overriding

        for i in sq:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)

print("The even numbers are ", even)
print("The odd numbers are ", odd)

    


    





            
