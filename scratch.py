list=[1,2,3,4,5,6]
print(list)
print(list.pop(-2))
print(list)


num=input("Enter two numbers for a range with space in between ")
num_list=num.split()


if len(num_list)==2: #ex: 10 20; next line defines range based on index value
    start=int(num_list[0]) #index of 0 is 10; so start = 10
    stop=int(num_list[1]) #indexval of 20 is 1; stop =20

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


