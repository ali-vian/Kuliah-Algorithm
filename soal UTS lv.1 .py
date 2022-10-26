# klasifikasi bilangan pembagi yang ganjil dan genap
n=int(input("Masukkan bilangan = "))
count=temp=''
for i in range(1,n+1):
    if n%i==0:
        if i%2==0:
            temp=temp+str(i)+" "
        else:
            count=count+str(i)+" "
print("Faktor ganjil = "+"["+count+"]")
print("Faktor genap = "+"["+temp+"]")

# klasifikasi huruf vokal,konsonan, dan spasi
inp=input("Masukkan karakter = ")
voc="a,i,u,e,o"
kos="b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z"
spc=" "
jml=count=temp=''
for i in inp:
    for j in voc:
        if i==j:
            temp=temp+str(i)+","
    for x in kos:
        if i==x:
            count=count+str(i)+","
    for z in spc:
        if i==z:
            jml=jml+str(i)+","
print("jumlah huruf vokal = [",temp,"]")
print("jumlah huruf konsonan = [",count,"]")
print("jumlah huruf spasi = [",jml,"]")