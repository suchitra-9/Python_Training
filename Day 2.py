#default datatype for input is string

a=int(input())
if(a%2==0):
    print("even")
else:
    print("odd")

a=str(input())
if len(a)<4:
    print("x")
else:
    print("y")

a=int(input())
if(a==1):
    print("monday")
elif(a==2):
    print("tuesday")
elif(a==3):
    print("wednesday")
elif(a==4):
    print("thursday")
elif(a==5):
    print("friday")
elif(a==6):
    print("saturday")
elif(a==7):
    print("sunday")
else:
     print("invalid")

a=int(input())
if a>0 and a<20:
    if a%2==0:
        print("weird number")
    else:
        print("normal number")
if a>=20 or a<30:
    print("normal number")
if a>=30:
    if a%2==0:
        print("even number")
    else:
        print("normal number")

sd={ 'r1':{'n':'sn1','p':'saddr1'},
     'r2':{'n':'sn2','p1':'saddr2'}}
 print(sd['r2'])

 l=[1,9,8,3]
for i in l:
    print(i**2)

i=5
l=[4,7,8,9]
temp=0
for i in range(len(l)):
    if i==l[i]:
        print(i)
        temp=1
        break

if temp==0:
        print("not found")

l=[x for x in range(1,101) if x%7==0 and x%11==0]
print(l)

for i in range(0,11):
    print(i)

arr=list(map(int,input().split(' ')))
p,n=0,0
for i in arr:
    if i<0:
        n+=1
    else:
        p+=1
print(p+n)
