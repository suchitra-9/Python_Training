a=int(input())
if(a%2==0):
    print("even")
else:
    print("odd")

l=[]
d={}
for i in range(2):
    d.update({
        'key1':input(),
        'key2':input()
    })
    l.append(d)
    print(d)
    print(l)

r=3
c=3
arr=[]
for i in range(r):
    ele=[]
    for j in range(c):
        ele.append(int(input()))
        arr.append(ele)
        print(arr)

r=3
c=3
arr=[]
for i in range(r):
    ele=[]
    for j in range(c):
        ele.append(int(input()))
        arr.append(ele)
        print(arr)

s='hello world'
print(s)
#split=''
print('-'.join(s))

.dot format,f format
num=10
print(f"the {num} is {num:.5f}")

a,b,c,d,e=int(input(),input(),input(),input(),input())
print(a,b,c,d,e)

a = int(input())
if a / 1 == 0 and a / a == 0:
    print("prime")
else:
    print("not prime")

print(4^7)