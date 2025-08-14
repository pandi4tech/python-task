# import math
# sqrt_val = math.sqrt(64)
# pi_const = math.pi
# print(sqrt_val)
# print(pi_const)

# import datetime
# # date_today = datetime.date.today()
# time_now = datetime.datetime.now().time()
# # print(date_today)
# print(time_now)

# import calendar
# cal_october = calendar.month(2005, 7)
# print(cal_october)

# def greeting(name):
#   print("Hello, " + name)
# pandi = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }

# import camelcase
# c = camelcase.CamelCase()
# txt = "hello world"
# print(c.hump(txt))

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def myfunc(self):
#     print("Hello my name is " + self.name)
# p1 = Person("John", 36)
# del p1.age
# print(p1.age)


# n=int(input("enter the number:"))
# if n%2!=0:
#     print("weird")
# elif n%2==0 :
#     if 2 <= n <= 5:
#         print("not weird")
#     elif 6 <= n <= 20:
#         print("weird")
#     elif n > 20:
#         print("not weird")   

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     c=a+b
#     d=a-b
#     e=a*b 
#     print(c,d,e)
    
# n=7
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i*j,end=" ")
#     print()

# word="pandi"
# print({char: ord(char) for char in word})

# def convert(lenght,formvalue,tovalue):
#     if formvalue=="km" and tovalue=="miles":
#         return lenght/1.6
#     elif formvalue=="miles" and tovalue=="km":
#         return lenght * 1.6
#     elif formvalue==tovalue:
#         return lenght
#     elif formvalue!="km" and tovalue!="miles":
#         return -1
#     elif tovalue!="km" and tovalue!="miles":
#         return -1
# print(convert(9,7,5))

# n=[1,2,3,4]
# for nu in n:
#     if nu % 2 == 0:
#         n.remove(nu)
# print(n)

# Create a base class Animal with a method make_sound().
# Create two subclasses Dog and Cat that override the make_sound() method.
# class animal:
#     def make_sound(self):
#         print("Some generic animal sound")
# class dog(animal):
#     def make_sound(self):
#         animal.make_sound(self)
#         print("woof!")
# class cat(animal):
#     def make_sound(self):
#         animal.make_sound(self)
#         print("meav")
# animals=dog()
# animals.make_sound()
# aniimal=cat()
# aniimal.make_sound()   

# Create a class Vehicle with attributes like brand, model, and a method start_engine(). 
# Then create a subclass Car and add an attribute num_doors.

# class cat:
#     def _init_(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(f"i am a cat.my name is {self.name}. i am {self.age} years old")
#     def make_sound(self):
#         print("meow")
# class dog:
#     def _init_(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(f"i am a dog.my name is {self.name}. i am {self.age} years old")
#     def make_sound(self):
#         print("bark")
# dog1=dog("puffy",4)
# cat1=cat("minnu",2)
# for animal in (cat1,dog1):
#     animal.info()
#     animal.make_sound()

# from abc import ABC, abstractmethod
# # Abstract Class
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
# # Concrete Class
# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"
# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"
# # Usage
# animals = [Dog(), Cat()]
# for animal in animals:
#     print(animal.make_sound())

# class Car():
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.engine_started = True

#     def startEngine(self):
#         if not self.engine_started:
#             print(f"Starting the {self.model}'s engine.")
#             self.engine_started = True
#         else:
#             print("Engine is already running.")
# obj=Car("heth","gwrge",2001)
# obj.startEngine()

# n = int(input(""))
# for i in range(n):
#     print (i*i)

# n = int(input())
# integer_list = map(int, input().split())
# t = tuple(integer_list)
# print(hash(t))



# n="pandi"
# reversede=n[::-1]
# print(reversede)


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(6))
