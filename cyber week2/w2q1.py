n=int(input("enter number:"))
c=0
for i in range(2,(n//2)+1):
    if(n%i==0):
        c=c+1
        break
if(c==0):
    print("is prime")
else:
    print("not a prime")
