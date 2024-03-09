### Phase 1
# for i in [1,2,3,4][::-1]:
#     print (i)
# else:
#     print("python")
    
# print(min(max(False,-3,-4),2,7))

# A=[[1,2,3],[4,5,[3,4,5,6]],[7,8,9]]
# print(A[1][2][3])

# l=[1,0,2,0,'hello','',[]]
# print(list(filter(bool,l)))

# print("-abc. DEF PyThon".capitalize())

# # a=set([[1,2],[3,4]])

# b=set((1,2,3,4))

# c=set([1,2,2,3,4])

# d={1,2,3,4}
# print(b,c,d)

# z=set('abc')
# print(z)
# z.add('san')
# print(z)
# z.update(set(['p','q']))
# print(z)

##Practise


# def check_armstrong(num):
#     '''This is the function to check the number is armstrong or not'''
#     r=0
#     z=num
#     num_str=str(num)
#     l=len(num_str)
#     while (num>0):
#         s=num%10
#         r=(s**l)+r
#         num=num//10
        
#     if (r==z):
#         print("armstrong number")
#     else:
#         print("not a armstrong")
    
    

# input_num=int(input("Enter the number"))
# check_armstrong(input_num)
    
    
# def check_prime(n):
#     count=0
#     for i in range(1,n):
#         if (n%i==0):
#             count += 1
#     if (count>1):
#         print("It is not a prime number")
#     else:
#         print("It is a prime number")
        
# check_prime(4)



# def check_palindrome(num):
#     '''This is the function to check the number is armstrong or not'''
#     r=0
#     z=num
 

#     while (num>0):
#         s=num%10
#         r=r*10+s
#         num=num//10
        
#     if (r==z):
#         print("palindrome number")
#     else:
#         print("not a palindrome")
    
    

# input_num=int(input("Enter the number"))
# check_palindrome(input_num)



# def check_prime(start,end):
#     '''Function to calculate the prime number in given range'''
#     while (start<=end):
#         if (start==0 or start==1):
#             pass
#         else:
#             count=0
#             for j in range(1,start):
#                     count += 1
#             if count > 1:
#                 pass
#             else:
#                 print(start)
#         start += 1
            
            
# def check_prime(n):
#     count=0
#     for i in range(1,n):
#         if (n%i==0):
#             count += 1
#     if (count>1):
#         pass
#     else:
#         print(n)
        
# start=int(input("enter the start range"))
# end=int(input("enter the end range"))

# while (start<=end):
#     if (start==0 or start==1):
#         pass
#     else:
#         check_prime(start)
#     start+=1
                    
                    
# def check_armstrong(n):
#     strN=str(n)
#     sum=0
#     lengthN=len(strN)
#     for i in strN:
#         sum=(int(i)**lengthN)+sum
#     if (sum==n):
#         print("Armstrong")
#     else:
#         print("Not a armstrong")
    


# input_num=int(input("Enter the number"))
# check_armstrong(input_num)
    
# def remove_bad(s):
#     bad_char=[";",":","*","!"] 
#     n=""
#     for i in s:
#         if (i in bad_char):
#             pass
#         else:
#             n = n+i
            
#     print(n)
            

# s="py:th!o:n;py*t*h!:o"
# remove_bad(s)

# l=[111,32,-9,-45,17,-19,87,0]
# def sep(*l):
#     newL=[]
#     for i in l:
#         if (i>0):
#             newL.append(i)
#         else:
#             pass
        
#     print(newL)
    
# sep(111,32,-9,-45,17,-19,87,0)


# a="nISCHAY DAI"
# b=a.capitalize()
# c=a.zfill(15)
# print(b)
# print(c)
# import random
# count=0
# while count<50:
#   print(random.randint(1,1000))
#   count += 1


# def sum(n):
#     sum=0
#     for i in n:
#         sum += i
#     print(sum)
    
# def sum2(n):
#     sum=0
#     i=0
#     while (len(n)>i):
#         sum += n[i]
#         i +=1
#     print(sum)
    
    
# list1=[1,2,3,4,5]
# sum2(list1)
# print(not(True))

# def fact(n):
#     '''This function gives the factorial of given number'''
#     i=1
#     fact=1
#     if (n==1 or n==0):
#         return 1
#     while (n>=i):
#         fact=fact*i
#         i+=1
#     return fact
            
        
        
# value=fact(5)
# print(F"The factorial of given number is {value}")
# print(fact.__doc__)

# def sep():
#     with open("c.txt","r") as f:
#         n=f.readlines()
#         print(n)
#         for i in n:
            
#             j=i.split()
#             for k in j:
#                 if len(k)>4:
#                     pass
#                 else:
#                     print(k)
            
# sep()


# with open("login.txt",'r') as f:
#     n=f.read()
#     with open("reg.txt","w") as g:
#         g.write(n)


# n=["text\n","hello"]
# with open("reg.txt","w") as g:
#     g.writelines(n)

# list1=[1,2,3,4]
# list1.insert(1,"w")
# n=list1.pop(1)
# a={'1':'w','2':'e'}
# a['1']='p'
# print(a)
# a.popitem()
# print(a)
# print(n)

# def my_function(*args, **kwargs):
#     print("Positional arguments (*args):", args)
#     print("Keyword arguments (**kwargs):", kwargs)

# # Example calls to the function
# my_function(1, 2, 3, name="Alice", age=30)


# def duplicate(n):
#     '''This function is used to delete duplicate data from a list'''
#     m=set(n)
#     new_list=list(m)
#     print(new_list)

# n=[1,2,3,4,1,2]
# duplicate(n)

# def reverseString(s):
#     '''Function to rever a string using palindrome'''
#     if len(s)==0:
#         return s
#     else:
#         return reverseString(s[1:])+s[0]
    
# output=reverseString("nischay")
# print(output)

# def bonus(salary,time_spent):
#     '''Fuction to calculate the bonus'''
#     print(salary,time_spent)
#     if (time_spent>10):
#         bonus=(10*salary)/100
#     elif (time_spent>=6 and time_spent<=10):
#         bonus=(8*salary)/100
#     else:
#         bonus=(5*salary)/100
        
#     print(f"The bonus is {bonus}")
    
    


# salary=int(input("Enter the salary"))
# time_spent=int(input("Enter the time spent by that employee"))
# bonus(salary,time_spent)

# def calculate(s):
#     spaceCount=0
#     digitCount=0
#     lettersCount=0
#     numbersCount=0
#     for i in s:
#         if (i.isdigit()):
#             digitCount += 1
#         elif (i.isspace()):
#             spaceCount += 1
#         elif (i.isalpha()):
#             lettersCount += 1
#         else:
#             numbersCount += 1
    
#     print(f"letters:{lettersCount} digit:{digitCount} space:{spaceCount} numbers:{numbersCount}")
            
# a="Hello I am Ai123 4.0 version"
# calculate(a)
    

    