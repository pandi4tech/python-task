# n=5
# for i in  range(n):
#     for j in range(i+1):
#         if j==0 or j==i or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=4
# m=0

# for i in range(1,n+1):
#     m+=i
#     print(m)
#     for j in range(1,i+1):
#         l+=0
#         print(l)
#     print()

# n=float(map(int,input("enter the number:".split())))
# print(n)

# n=12.3, 13.4

# n=5 
# for i in range(1,n+1):
   
#     for j in range(1,n+1):

#         print(f"{i*j:2}",end="  ")
#     print()

# n=5
# for i in range(n,0,-1):
#     print(i,end="  ")
#     for j in range(n-1,0,-1):
#          print(j,end="  ")
#     print()

# n=5
# for  i in range(n,0,-1):
#     for j in range(i):
#             print((i-j),end=" ")
#     print()


# n=5
# # a=5
# for  i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for j in range(1,i+1):   
#         print(j,end=" ")
#     print()  


# for i in range(1,6):
#     a=5
#     for j in range(1,6):
#         print(a,end=" ")
#         a=a-1
#     print()

# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# def greet(name):
#     print("hello,"+name)
# a={"name":"jon","age":36}

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
# create()

# class studyhall:
#     def student(self):
#         print("student study time is going on")
#     def lecture(self):
#         print("in order to guide student lecture is now available in study hall")
# studentnila=studyhall()
# lecturesona=studyhall()
# studentnila.student()
# lecturesona.lecture()

# class studyhall:
#     name="sona"
#     def student(self):
#         print("student study time is going on")
#     def lecture(self):
#         print("in order to guide student lecture is now available in study hall")
# studentnila=studyhall()
# lecturesona=studyhall()
# studentnila.lecture()
# lecturesona.student()
# studentnila.name="bharvathi"
# print(studentnila.name)

# class cars:
#     car="1 = BMW","2 = ROLLS ROYCS","3 = MARUTI SUZUKI "
#     print(car)
#     def bmw(self):
#         return f"Rs-5000000"
#     def rolls_roycs(self):
#         return f"ROLLS ROYCS : Rs-10000000"
#     def Maruti_Suzuki(self):
#         return f"MARUTI SUZUKI : Rs-2500000"
# cardetails=cars()
# car=int(input("enter the car rgno 1 to 3 :"))
# if car==1:
#     print(cardetails.bmw())
# elif car==2:
#     print(cardetails.rolls_roycs())
# elif car==3:
#     print(cardetails.Maruti_Suzuki())
# else:
#     print("there are no cars in the numbers")

# car=["BMW","ROLLS ROYCS","MARUTI SUZUKI "]
# print(car[1])

# class laptap:
#     def __init__(self):
#         print("manibharathi")
#     def display(self):
#         print("display")
# hp=laptap()
# hp.display()

# def two_sum(nums, target):
#     num_to_index = {}  
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_to_index:
#             return [num_to_index[complement], i]
#         num_to_index[num] = i
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target)) 

# def maxCostOfLaptopCount(cost, labels, dailyCount):
#     n = len(cost)
#     max_cost = 0
#     i = 0

#     while i < n:
#         day_cost = 0
#         legal_count = 0

#         while i < n and legal_count < dailyCount:
#             day_cost += cost[i]
#             if labels[i] == "legal":
#                 legal_count += 1
#             i += 1

#         if legal_count == dailyCount:
#             max_cost = max(max_cost, day_cost)

#     return max_cost

# # Example usage:
# cost = [2, 5, 3, 11, 1]
# labels = ["legal", "illegal", "legal", "illegal", "legal"]
# dailyCount = 2

# print(maxCostOfLaptopCount(cost, labels, dailyCount))  # Output should be 10