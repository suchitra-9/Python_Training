#Datatypes
x=1
z=[a,b]
a=(1,)#tuple it's immutable
b=(1)#int
s={'a','b','c','a'}#sets don't follow insertion order and repeted value
print(type(a))
print(type(b))
print(type(z))
print(type(s))

#arthimetic opertors
a=1+2
b=10-4
c=10*10
d1=5%2#modular
d2=4/2# div
d3=3//2#int div quotient
print(a,b,c,d1,d2,d3)

#membership operators(in,not in)
l=[1,2,3,4,5,5]
print(1 in l)

#identity operator(is ,not is)None or not
a=1
print(a is 1)

#list operations
list=[1,2,5]
list.append(10)

#we can append only 1 value at a time
print(list)
print(len(list))#length
print(list.remove(2))#value,value is mandatory,it directly removes the value and returns none
print(list.pop(1))#index,index optional,enter the remaining values

#insert(index,element)
list=[1,2,3,4,5]
print(list)
print(list.insert(3,7))

#copy
a=[10,20,30]
b=a.copy()
b[0]=100
print(a)

#clear
b=a.clear()
print(a)

#reverse
a=[10,20,30]
b=a.reverse()
print(a)

#sort
a=[10,20,30]
b=a.sort(reverse=False)
print(a)

#sorted
a=[100,20,30]
b=sorted(a,reverse=True)
print(b)
print(a)

#type conversion
a="hi"
b=str(12)
c=a+b
print(c)

a=list('12345')
print(a)
b=list(map(int,a))
print(b)