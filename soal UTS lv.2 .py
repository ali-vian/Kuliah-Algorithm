# mancari pembagi yang sama dan yang sama terbesar

a=int(input("bilangan pertama = "))
b=int(input("bilangan kedua = "))
temp=[]
count=[]
for i in range(1,a+1):
    if a%i==0:
        count.append(str(i))
for j in range(1,b+1):
    if b%j==0:
        temp.append(str(j))
print(temp)
print(count)
s=0
for k in count:
    for l in temp:
        if l==k and l!='1':
            s+=1
            print("pembagi yang sama -",s,"=",l)
            xx=l
print("pembagi yang sama yang terbesar adalah ",xx)