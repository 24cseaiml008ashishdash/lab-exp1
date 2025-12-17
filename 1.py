a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))
d=int(input("Enter the number"))
e=int(input("Enter the number"))
f=int(input("Enter the number"))
g=int(input("Enter the number"))

mean=(a+b+c+d+e+f+g)/7
print("mean of the seven(7) numbers are:- ",mean)
n =[a,b,c,d,e,f,g] 
m=len(n) 
if(m%2==0):
     m1 = n[m//2] 
     m2 = n[m//2 - 1] 
     med = (m1+ m2)/2
else:
     med=n[m//2] 
print("median of the numbers are:- ",med)

mode=max(set(n),key=n.count)
print("mode of the numbers are:-",mode)

