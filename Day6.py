pip install translate

from translate import Translator

obj = Translator(from_lang="English", to_lang="Hindi")
new_name = obj.translate("Suchi")
print(new_name)


from translate import Translator

obj = Translator(from_lang="english", to_lang="spanish")
new_name = obj.translate("Suchi")
print(new_name)

def m1(a,b):
    print(a+b)
def m1(a,b,c):
    print(a+b+c)
print(m1(10,20,30))


class A:
    def m1(a,b):
        print(a+b)
class B(A):
    def m1(a,b,c):
        print(a+b+c)
print(m1(10,20,30))


class Animal:
    def speak(self):
        return ("speaks")


class Dog(Animal):
    def speak(self):
        return ("barks")
        pass


class Cat(Animal):
    def speak(self):
        return ("meow")


obj = Cat()
obj2 = Dog()
print(obj2.speak())
print(obj.speak())


class Animal:
    def speak(self):
        return ("speaks")


class Dog(Animal):
    def speak(self):
        return ("barks")
        pass


class Cat(Animal):
    def speak(self):
        return ("meow")


obj = Cat()
obj2 = Dog()
print(obj2.speak())
print(obj.speak())
