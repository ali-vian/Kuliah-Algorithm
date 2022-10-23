# lv. 0

#  soal 1 membuat deret [20 24 28 32 36 40 44] 
n=int(input("Banyaknya bilangan = "))
a=int(input("Masukkan bilangan pertama = "))
temp=''
for i in range(n):
    x=a+4
    temp=temp+str(a)+" "
    a=x
print("[",temp,"]")

# soal 2 membuat deret [4 8 12 16 20 24 28 32 36 40 ]
n=int(input("Banyaknya bilangan = "))
a=int(input("Masukkan bilangan pertama = "))
temp=''
for i in range(a,n*4+a,4):
    temp=temp+str(i)+" "
print("["+temp+"]")

#soal 3 membuat deret [ 1 -2 3 -4 5 -6 7 -8 9 -10  ]
n=int(input("Masukkan batas = "))
a=0
temp=''
for i in range(1,n+1,2):
    a=a-2
    temp=temp+str(i)+' '+str(a)+' '
print("[",temp,"]")

#soal 4 membuat deret [0 2 4 6 8 10 12 14 16 18 ] 
n=int(input("Banyaknya bilangan = "))
temp=''
for i in range(0,n*2,2):
    temp=temp+str(i)+" "
print("["+temp+']')

# soal 5 membuat deret [0 5 10 15 20 25 30 35 40 45 ]
n=int(input("Banyaknya bilangan = "))
temp=''
for i in range(0,n*5,5):
    temp=temp+str(i)+' '
print("["+temp+"]")

#soal 6 [ 0 -1 2 -3 4 -5 6 -7 8 -9  ]
n=int(input("Banyaknya bilangan = "))
temp=''
x=1
for i in range(0,n,2):
    x-=2
    temp=temp+str(i)+" "+str(x)+" "
print("[",temp,"]")
