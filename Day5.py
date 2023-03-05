n=int(input())
arr=[]
for i in range(n):
    a=input().split()
    if a[0]=="add":
        arr.append(int(a[1]))
    elif a[0]=="insert":
        ele=int(a[1])
        ind=int(a[2])
        arr.insert(ind,ele)
    elif a[0]=="remove":
          ele=int(a[1])
          if ele in arr:
                arr.remove(ele)
    elif a[0]=="pop":
          if len(arr)>0:
                 arr.pop()
    elif a[0]=="print":
          if len(arr)!=0:
                       print(*arr)


                       class A:
                           name = "me"
                           age = 12


                       class B(A):
                           age = 23


                       obj = B()
                       obj.name = "i"
                       print(obj.age)
                       print(obj.name)


                       class A:
                           name = "me"
                           age = 12


                       class B(A):
                           age = 23


                       class C(B):
                           pass


                       class D(C):
                           pass


                       obj = D()
                       obj = B()
                       obj = C()
                       obj.name = "i"
                       print(obj.age)
                       print(obj.name)


    class Principal:
        name = "xyz"
        salary = 123
        age = 54


    class Hod(Principal):
        name = "abc"
        salary = 456


    class Tpo(Hod):
        name = "asd"


    class Faculty(Tpo):
        pass


    obj = Hod()
    obj = Tpo()
    print(obj.name)
    print(obj.salary)
    print(obj.age)


    class Owner:
        name = "abc"
        age = 45
        income = 4000


    class Customer1(Owner):
        cost = 600
        items = 8


    class Customer2(Owner):
        cost = 800
        cover = 3


    class Customer3(Owner):
        cost = 9


    obj1 = Customer1()
    obj2 = Customer2()
    obj3 = Customer3()
    print(obj2.cost)
    print(obj.income)
    print(obj1.items)
    print(obj3.age)


    class Father:
        # def m1(self):
        name = "abc"
        age = 45


    class Mother:
        name = "xyz"
        age = 34


    class Child(Father, Mother):
        name = "pty"


    obj = Child()
    print(obj.age)


    class Owner:
        name = "abc"
        age = 45
        income = 4000


    class Father(Owner):

        name = "abc"
        age = 45


    class Mother(Owner):
        name = "xyz"
        age = 34


    class Child(Father, Mother):
        name = "pty"


    obj = Child()
    obj1 = Father()
    obj2 = Mother()
    print(obj1.age)
    print(obj2.income)
    print(obj.name)
    print(obj.age)


#random
from random import random,randint
a=randint(1,20)
print(a)

from random import random, randint

p1 = 0
c1 = 0
l = 3
p1 = input("enter a choice")
p2 = input("enter a choice")
if x == 1 and y == 2:
    print("paper")
elif x and z:
    print("rock")
elif y and z:
    print("scissor")
else:
    print("invalid input")


# polymorphism
class A:
    def method_1(self, a, b):
        print("sum", a + b)


class B(A):
    def method_1(self, a, b):
        print("pro", a * b)


obj = B()
obj.method_1(10, 20)

#swap 0 and 1
a=int(input())
b=int(input())
bin(a)
bin(b)
print(bin(a))
print(bin(b))
swap(0,1
print(bin(a))
print(a^b)

n - int(input())

arr = []

for i in range(n):
    a = input().split()
if a[0] == "add":
    arr.append(int(a[1]))

elif a[0] == "insert":
    ele = int(a[1])
ind = int(a[2])
arr.insert(ind, ele)
elif a[0] == "remove":

ele = int(a[1])
elif ele in arr:

arr.remove(ele)

elif a[0] == "pop":
if len(arr) > 0:

    arr.pop() elif a[0]="print":

    if
len(arr) = 0: print("arr)

else: print("Invalid Input")