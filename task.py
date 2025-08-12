"""task using simple print statement"""

# a=input("enter the name:")
# b=input("enter the age:")
# print("hello,my name is",a,"and i am",b,"old")

# a=int(input("enter the number1:"))
# b=int(input("enter the number2:"))
# c=int(input("enter the number3:"))
# print(a,b,c,sep="-")

# a=input("enter the number:")
# b=input("enter the number:")
# print(a+b)

"""task using casting types"""

# x=input("enter the number:")
# y=int(x)
# print(y)
# print(type(y))

# x=list(input("enter the number:"))
# y=tuple(x)
# print(y)
# print(type(y))

# a,b=map(float,(input("enter the two numbers between a space:").split()))
# z=a+b
# y=int(z)
# print(y)

# a=set(map(int,(input("enter the numbers:").split())))
# b=sum(a)
# print(b)

# a=list(map(int,(input("enter the numbers:").split())))
# a.sort()
# print(a)

"""task using if statement"""

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))
# if a >= b and a >= c :
#     print("a is a largest no")
# elif b >= a and b >= c:
#      print("b is a largest no")
# else:
#      print("c is a largest no")

# a=int(input("enter the number:"))
# if a >= 18:
#     print("a person is eligible to vote")
# else:
#     print("a person is not eligible to vote")

# a=int(input("enter the number:"))
# if a%2==0:
#     print ("a number is even")
# else:
#         print("a number ia not even")

# a=int(input("enter the number:"))
# if 85 < a and a <= 100:
#     print("grade A")
# elif 60 < a and a <= 85:
#     print("grade B")
# elif 40 < a and a <= 60:
#     print("grade C")
# elif 35 < a and a <= 40:
#     print("grade D")
# else:
#     print("fail")

# a=str(input("enter the word:"))
# b=str(input("enter the word:"))
# if b in a:
#     print("it is present")
# else:
#     print("it is not present")

# a=int(input("enter the number:"))
# if a%4==0:
#     print("it is leaf year")
# else:
#     print("it is not leaf year")

"""task using for loop""" 

# a="hello world"
# for i in a:
#     print(i)

# for i in range(1,10):
#      print (i,end=" ")
#      if i == 5:
#         break

# for i in range(1,10):
#     if i%2!=0:
#        print(i)
    
# for i in range(1,10):
#     if i%2==0:
#        print(i)
    
"""task using while loop""" 

# i=1
# while (i<=10):
#     print(i)
#     i+=1
#     continue

# n=int(input("enter the number:"))
# i=1
# m=0
# while(i<=n):
#     m+=i
#     i+=1
#     print(f"{n}:{m}")

# n=int(input("enter the number:"))
# i=1
# f=1
# while i<=n:
#     f*=i
#     i+=1
#     print(f)
    # print(f"factorial of {n}is {factorial}")

# n=int(input("enter the number:"))
# i=2
# f=True
# while i<=n//2:
#     if n%i==0:
#         f=False
#         break
#     i+=1
# if f and n>1:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")

# n=int(input("enter the number:"))
# i=0
# while n>0:
#     digit=n%10
#     i=i*10+digit
#     n=n//10
#     print(i)

# n=int(input("enter the number:"))
# i=0
# while n>0:
#     n=n//10
#     i+=1
#     print(i)

# n=int(input("enter the number:"))
# i=0
# while n>0:
#     j=n%10
#     n+=j
#     n=n//10
#     i+=1
#     print(i)

# n=int(input("enter the number:"))
# i=1
# while n<10:
#     print(f"{n}x{i}={n*i}")
#     i+=1

# n=int(input("enter the number:"))
# a,b=0,1
# i=0
# while i<n:
#     print(a,end=" ")
#     a,b=b,a+b
#     i+=1

# n=int(input("enter the start number countdown:"))
# while n>=0:
#     print(n)
#     n-=1

"""for loop number pattern program"""

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print('*',end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(i,n+0):
#         print('*',end=" ")
#     print()

n=5
for i in range(1,n+1):
    print('*'*i)

# n=5
# for i in range(n,0,-1):
#     print('*'*i)

# n=5
# for i in range(1,n+1):
#     print(' '*(n-i), end="")
#     print( "*"*(2*(i-1)+1))

# n=5
# for i in range(1,n+1):
#     print(' '*(i-1), end="")
#     print( "*"*(2*(n-i)+1))

# n=5
# for i in range(1,n+1):
#     print(' '*(n-i) + "*"*(2*(i-1)+1))
# for i in range(n-1,0,-1):
#         print(' '*(n-i) + "*"*(2*(i-1)+1))

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(end=" ")
#     for j in range(i*1):
#         print(j+1,end=" ")
#     print()

# n=5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(end=" ")
#     for j in range(i*1):
#         print(j+1,end=" ")
#     print()

# n=5
# m=1
# for i in range(1,n+1):
#  for j in range(1,i+1):
#     print(f"{m:2}",end=" ")
#     m+=1
#  print()

# n=5
# for i in  range(n):
#     for j in range(i+1):
#         if j==0 or j==i or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or j==n-1 or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         if j%2==0:
#            print ("*",end="")
#         else:
#             print("_",end="")
#     print()


"""task using function program """

# def create():
#     x=int (input("enter the number:"))
#     if x>0:
#         print("it is positive number")
#     elif x==0:
#         print("it is zero")
#     else:
#         print("it is negative number")
# create()

# def create():
#     x=int (input("enter the number:"))
#     y=int (input("enter the number:"))
#     print("addition:",x+y)
#     print("subtraction:",x-y)
#     print("multiplication:",x*y)
#     print("division:",x/y)
#     print("module:",x%y)
#     print("floor division:",x//y)
#     print("exponentiation:",x**y)
# create()

# z=lambda x:x+4
# print(z(5))

# a=lambda x,y:x*y
# print(a(5,2))

# def func(n):
#     a=0
#     b=1
#     print(f"{a} {b}",end=" ")
#     for i in range(n):
#         c=a+b
#         a=b
#         b=c
#         print(c,end=" ")
# func(8)

# def sr():
#     n=int(input("enter the number:"))
#     print(f"{n} square root is {n**0.5}")
# sr()

# def greet(name):
#     print(f"hello, {name}!")
# greet("world")

# def sum_of_two(a,b):
#     a=int(input("enter the number:"))
#     b=int(input("enter the number:"))
#     return a+b
# print(sum_of_two(4,9))

# def welcome_message(name,message="welcome!"):
#     print(name,message)
# welcome_message("sathya")
# welcome_message("sathya your")

# def create(name,age,city):
#     print(f"my name is {name},i am {age} year old,and i live in {city}.")
# create("sathosh",22,"pudukkottai")

# def average(*numbers):
#     a=sum(numbers)/len(numbers)
#     print(sum(numbers))
#     print(len(numbers))
#     return(a)
# print(average(44,5,4,34,56))

# def double_element(lst):
    # a=list(map(int,input("enter the number:").split()))
#     return list(i*2 for i in lst)
# print(double_element([5,4,3]))

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("enter the number:"))
# print(fact(n))

# def swep(a,b):
#     print(f"a:{a}  b:{b}")
#     # print("a:",a)
#     # print("b:",b)
#     a,b=b,a
#     print(f"a:{a}  b:{b}")
#     # print("a:",a)
#     # print("b:",b)
# swep(10,20)

# z=lambda x,y:x*y
# result=z(3,2)
# print(f"the result is {result}")

# def apply_function(f,x):
#     return f(x)
# def square(x):
#     return x*x
# print(apply_function(square,4)

# def is_palindrom(word):
#     if word==word[::-1]:
#         print(f"{word} is a palindrome")
#     else:
#         print(f"{word} is not a palindrome")
# is_palindrom("pandi")

# def is_prime(n):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 print(f"{n} is not a prime number.")
#                 break
#         else:
#             print(f"{n} is a prime number.")
# is_prime(89)

# def divide(x,y):
#     if y==0:
#         print("Error:Division by zero!")
#     else:
#         print(f"{x/y}")
# divide(10,0)

# def vowel(s):
#     vowel="aeiouAEIOU"
#     return sum(1 for i in s if i in vowel)
# print(vowel("hello world!"))

# def vowels(s):
#     print(s)
#     count=0
#     for i in range vowels:
#         if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#             v=str.count(s)
#             print(v)
#         else:
#             print("not have any vowel character")
# vowels("hello, world!")

# def create(a,b,c):
#     return max(a,b,c)
# print(create(10,7,12))

"""task using class and object program """

# class person:
#     def info(self):
#         name=(input("enter the name:"))
#         print("hello, my name is", name)
#     def info1(self):
#         age=int(input("enter the number:"))
#         print("i am",  age ,"years old")
#     def info2(self):
#         address=(input("enter the name:")) 
#         print("i am coming from", address )  
# a=person()
# a.info()
# a.info1()
# a.info2()

# class person:
#     def __init__(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address
#     def greet(self):
#         print(f"hello,my name is {self.name}")
#     def info(self):
#         print(f"Name : {self.name} , Age : {self.age} , Address : {self.address}")
# name=input("enter the name:")
# age=int(input("enter the number:"))
# address=input("enter the name:")
# personinfo=person(name,age,address)
# personinfo.greet()
# personinfo.info()

# class BankAccount:
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.balance=balance
#         print(f"tha account_holder name is {self.account_holder}")
#         print(f"the {self.account_holder} balance is {self.balance}")
#     def deposit(self,amount1):
#         self.balance+=amount1
#         print(f"the deposit amount is {amount1}")
#         print(f"after deposit current balance is {self.balance}")
#     def withdraw(self,amount):
#         self.balance-=amount
#         print(f"the withdraw amount is {amount}")
#     def check_balance(self):
#         return f"tha current balance is {self.balance} "
# bankdetail=BankAccount("mani bharathi",10000)
# bankdetail.deposit(5000)
# bankdetail.withdraw(7000)
# print(bankdetail.check_balance())

# class rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         a=self.length * self.width
#         return f"the area of the rectangle is {a}"
#     def perimeter(self):
#         p=2 * (self.length + self.width)
#         return f"the area of the rectangle is {p}"
# length=int(input("enter the number:"))
# width=int(input("enter the number:"))
# shape=rectangle(length,width)
# print(shape.area())
# print(shape.perimeter())

# class book:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
#     def book_info(self):
#         return f"The Book's {title} , {author} , and {price}"
# title=input("Enter the title : ")
# author=input("Enter the author name : ")
# price=int(input("Enter the price : "))
# bookdetail=book(title,author,price)
# print(bookdetail.book_info())

# class student:
#     def __init__(self,name,roll_no,mark):
#         self.name=name
#         self.roll_no=roll_no
#         self.mark=mark
#         print(f"The student name is {name}")
#         print(f"{name} roll number is {roll_no}")
#         print(f"mark:",mark)
#     def total_marks(self):
#         total=sum(self.mark.values())
#         return f"the total mark is {total}"
#     def average_marks(self):
#         total=sum(self.mark.values())
#         avg=total/len(self.mark)
#         return f"the average of the marks is {avg}"
# studentdetail=student("Pandi","22cs3240",{"tamil":82,"english":79,"maths":97,"science":84,"social science":74})
# print(studentdetail.total_marks())
# print(studentdetail.average_marks())

# class car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#     def car_info(self):
#         print(f"\ncardetails: \n\nmake : {self.make} \nmodel : {self.model} \nyear : {self.year}" )
# cardetails1=car("toyota","Corolla",2020)
# cardetails2=car("honda","Civic",2022)
# cardetails3=car("ford","mustang",2021)
# cardetails1.car_info()
# cardetails2.car_info()
# cardetails3.car_info()

# import time
# class timer:
#     def __init__(self,start_time):
#         self.start_time=start_time
#         print(f"starting time = {start_time}")
#     def start(self):
#         self.current=time.time()
#         return f"current time is {self.current}"
#     def elapsed_time(self):
#         self.elapsed=self.current - self.start_time
#         return f"the time elapsed is {self.elapsed}"
# timercal=timer(8.00)
# print(timercal.start())
# print(timercal.elapsed_time())

# class shoppingcart:
#     def _init_(self):
#         self.items=[]
#     def add_items(self,name,price):
#         self.name=name
#         self.price=price
#         self.items.append({"name":name,"price":price})
#         print(f"name:{name},price:{price}")
#     def total_price(self):
#         return f"total price: {sum(item["price"] for item in self.items)}"    
# cart=shoppingcart()
# cart.add_items("apple",20)
# cart.add_items("orange",10)
# cart.add_items("banana",7)
# print(cart.total_price())

# class BankAccount:
#     def _init_(self,balance=0):
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#         print(f"the deposit amount is {amount}")
#     def withdraw1(self,amount1):
#         if self.balance>=amount1:
#             self.balance-=amount1
#             print(f"the withdraw amount is {amount1}")
#         else:
#             print("insufficient funds.")
#     def check_balance(self):
#         return f"tha current balance is {self.balance} "
# class person:
#     def _init_(self,name,account):
#         self.name=name
#         self.account=account
#     def deposit(self,amount):
#         self.amount=amount
#     def withdraw(self,amount):
#         self.amount.withdraw(amount)
#     def check_balance(self):
#         return f"{self.name}'s balance is {self.amount.check_balance()} "
# bankdetails=BankAccount(1000)
# persons=person("pandi",bankdetails)
# persons.deposit(5000)
# persons.withdraw(1000)
# persons.check_balance()

# class temperatureconverter:
#     def celsius_to_fahrenheit(celsius):
#         return f"{(celsius*9/5)+32}"
#     def fahrenheit_to_celsius(fahrenheit):
#         return f"{(fahrenheit-32)*5/9}"
#     def celsius_to_kelvin(celsius):
#         return f"{celsius + 273.15}"
#     def kelvin_to_celsius(kelvin):
#         return f"{kelvin - 273.15}"
# print(temperatureconverter.celsius_to_fahrenheit(25))
# print(temperatureconverter.fahrenheit_to_celsius(77))
# print(temperatureconverter.celsius_to_kelvin(25))
# print(temperatureconverter.kelvin_to_celsius(298.15))

"""task using OOPs program """

# class animal:
#     def speaker(self):
#         print("the cat meows")
# class cat(animal):
#     def name(self):
#         self.name="minuu"
#         return f"the cat name is {self.name}"
#     def color(self):
#         self.color="blue"
#         return f"the cat color is {self.color}"
# pet=cat()
# print(pet.name())
# print(pet.color())
# pet.speaker()

# class person:
#     def details(self,name,age):
#         self.name=name
#         self.age=age
#         print (f"my name is {name}")
#         print(f"i am {age} years old")
# class student(person):
#     def grade(self):
#         self.grade="A+"
#         print(f"he got a {self.grade} grade")
# det=student()
# det.details("john",18)
# det.grade()

# class parent:
#     def _init_(self,name,age):
#         self.name=name
#         self.age=age
#         print("parent initialize")
#     def speak(self):
#         print("parent speak")
# class child(parent):
#     def _init_(self,name,age):
#         super()._init_(name,age)
#         self.age=age
#         print("child initialize")
#     def speak(self):
#         print("child speak")
# Parent=parent("jon",23)
# Child=child("aline",32)
# Parent.speak()
# Child.speak()

'''basic class & object task '''
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def details(self):
#         print(f"my name is {self.name} \ni am {self.age} years old")
# detail=person("santhiya",12)
# detail.details()

# class rectangle:
#     def __init__(self,length,width):
#         self.length=length 
#         self.width=width
#     def calculation(self):
#         print(f"area of rectangle = {self.length * self.width}")
#         print(f"perimeter of rectangle = {2*(self.length + self.width)}")
# cal=rectangle(20,32)
# cal.calculation()

# class book:
#     def __init__(self,title,author):
#         self.title=title 
#         self.author=author
#     def book_info(self):
#         return f"the book title is {self.title}"

