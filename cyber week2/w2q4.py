n=int(input("enter digit:"))
for i in range(10**(n-1),10**n -1):
    sum=0
    temp=i
    while(temp!=0):
        rem=temp%10
        sum=sum+(rem**n)
        temp=temp//10
    if(sum==i):
        print(i, "is armstrong")
    

