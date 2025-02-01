def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
a=int(input("enter number"))
b=int(input("enter number"))
result=gcd(a,b)
if result==1:
    print(f"{a} and {b} are relatively prime")
else:
    print(f"{a} and {b} are not relatively prime")    
