# lec. 6
#Functions in Python:- Block of statements that perform a specific task

def calc_sum(a, b):
   return a + b
   
sum = calc_sum(12,13)
print(sum)
sum = calc_sum(2,3)
print(sum)   

def print_hello():
    print("hello")
    
print_hello()    
print_hello()
print_hello()
print_hello()

output = print_hello()
print(output)

#we want a function can do the average of 3 numbers
def calc_avg(a, b, c):
    sum = a+b+c
    avg = sum / 3
    print(avg)
    return avg
     
calc_avg(1,6,2)    
calc_avg(9,8,5)
    
#types of function 

#built-in fuction

#print is a fuction here
print("Dhruv", end=" ") #sep =" "
#if there was not a end=" ", then this is not come at one line.
print("Sneha") #end = "\n"
#len(),type(),range()

# user defined function are made as per the your coding need 

#Default Parameters :- it is use when we didn't want to give a value in fuction 
def cal_prod(a=2, b=1):    #whenever we want to give a default value, so give it from back 
    print(a*b)
    return a * b
    
cal_prod(3)    # here 3 is consider as a arrgument of the function at "a"

#Let's Practice 
#q1
cities = ["surat","mumbai","delhi","noida","dolakpur"]
dreams = ["Enterpunership","Family","Sneha","Child","House","Car"]

print(dreams[0], end=",")
print(dreams[2])

def print_len(list):
    print(len(list))
    
print_len(cities)
print_len(dreams)

def print_list(list):
    for items in list:
        print(items, end=" ")
        
print_list(dreams)
print()

#q3

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i 
    print(fact) 
                 
cal_fact(5)

#q4 
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(1)    
converter(80)

#q5
def Num(X):
    if(X % 2 == 0):
        return "Even"
    else:
        return "odd" 
print(Num(int(input("X :- "))))


# Recursion :- when a function calls itself repeatedly.

def show(n):
    print(n)

show(5)        #in this function there is no recursion
#if we want to show 5,4,3,2,1 in a single show function, then for that we need a recursion here. we can also run loop here  

#this function is known as recursion :- in this we complasior need a condition for stop 
def viva(x):
    if (x == 0):        #this is basecase
        return         # aagar yaha per "if" condition aur "return" nahi huha toh recursion infinty run kar rega fir vo saari memory occupied kar lega phir system error show kar dega. that why hame dono ko use karna jaruri hai.       
    print(x)
    viva(x-1)

viva(7)
     
def fact(n):
       if(n == 1 or n ==0):
               return 1
       return fact(n-1) * n
       
print(fact(6))

#Practice Question
#Q1
def calc_sum(a):
    if(a == 0):
            return 0
    return calc_sum(a-1) + a

sum = calc_sum(int(input("a = ")))
print(sum)

#Q2
def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)                                                                                

fruits = ["Mango","Litchi","Apple","Banana"] 
print_list(fruits)
#end of lec.6
