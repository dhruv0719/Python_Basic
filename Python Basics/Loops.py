# lec 5

#Loops in Python = repeat instructions.

#While Loops
count = 1
while count <= 5 :        # in this "count" variable is known as iterator 
    print("hello")
    count += 1
print(count)
    
Q = 1
while Q<=3:
    print("JAI SHREE RAM" , Q)
    Q+=1

print("Finish")

a = 5
while a >= 1:
    print(a)
    a -= 1 
print("i loop is ended")

# question on while loop 

#q1
w = 1 
while w <= 100:
     print(w)
     w += 1
print("end of q1")          

#q2
e = 100
while e>=1:
           print(e)
           e -= 1                            
print("end of q2")

#q3 
n = int(input("n :-"))
i =  1
while i <= 10:                                                                              
    print(n*i)
    i += 1                                                                                                       
print("end of table :-", n)

#Q4
nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(nums):
    print(nums [idx])
    idx += 1

print("End od Q4-A")

heroes = ["ironman","batman","spiderman","hulk","thor"]    #in this we are travel on the values of tuples/list, so this in programming is known as "TRAVERSE"
idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1                                                                                                                                   
print("End of Q4-B")

#Q5
tup = (1,4,9,16,25,36,49,64,81,100)
x = 49
s = 0 
while s < len(tup):
    if(tup[s] == x):
        print("Found at idx", s)
    else:
        print("Finding...")                                 
    s += 1                                            
print("End of Q5")                                                                                        
                                                                                                                                    
# Break & Continue
 
#Break :- it is use when we give condition in a loop, after that condition the loops is end and this is the use of break
t = 1
while t < 5 :
    print(t)
    if(t == 3):
               break                               
    t += 1
print("end of 't' loop")

tup = (1,4,9,16,25,36,49,64,81,100)
x = 49
s = 0                                                                                                      
while s < len(tup):
    if(tup[s] == x):
        print("Found at idx", s)
        break
    else: 
        print("Finding...")                             
    s += 1                                            
print("end of 'tup' loop")

#Continue :- it's is act as skip, if the condtion is applyed then the next comant is skipped  

f = 0 
while f <= 5:
    if(f == 3):
        f += 1 
        continue
    print(f)
    f += 1
print("end of 'f' loop")

x = 1
while x <= 10:
    if(x%2 == 0):
        x += 1 
        continue
    print(x)
    x += 1
print("this are odd no.")

x = 1
while x <= 10:
    if(x%2 != 0):
        x += 1 
        continue
    print(x)
    x += 1
print("this are even no.")
print("end of while loop")

# For loop :- it is used for sequential traversal. 

nums = [1,2,3,4,5]
for val in nums:
    print(val)
    
junk = ["pavbaaji","panner tika","fried rice","panipuri","pizza","bugar"]
for val in junk:
    print(val)

tup = (5,98,6,5,6,525,58)
for num in tup:
    print(num)

str = "Sneha and Dhruv"
for char in str:
    if( char == 'u'):
        print("u found")
        break
    print(char)                                                                                                   
else:                            #if we didn't write else here then there "End" is print    in break condition, but there was else in break condition then if we get a that, then loop is stop on that value.  
    print("End")                                                              
                                                                  
# Practice Question 
#q1
p = [1,4,9,16,25,36,49,64,81,100]
for val in p:
    print(val)
print("end of q1")
             
#q2
j = (1,4,9,16,25,36,49,64,81,100,36)
x = 36
idx = 0
for el in j:
    if (el == x):
        print("no. found at idx", idx)
        break             #if want that, when a element is found at once and we didn't to contiune on other same element. then we are use "break".    if we didn't did this then the other element are also got shown in output. 
        idx += 1        
            
            
#Range :- it is returns a sequence of no. , starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

print(range(5))

for i in range(7):    #range(stop)
    print(i)
print("end")

for i in range(1,7):    #range(start, stop)
    print(i)
print("end")

for i in range(2,7,3):    #range(start, stop, step)
    print(i)
print("end")

for s in range (0,100,2):
    print(s)
print("end of even no.")

for s in range (1,100,2):
    print(s)
print("end of odd no.")

# question 

#Que1 
for q in range (1,101):
    print(q)
print("end of Que1")    

#Que2
for w in range (100, 0, -1):
    print(w)
print("end ofQue2")

#Que3
z = int(input("z :- "))
for i in range(z, z*11,z):
    print(i)
print("end of Que3")

#Pass Statement :- this mean null statement, isko hum waha per use karte hai jaha per hame loop me koi kaam na karana ho. 
#pass is use for future code work

for c in range(5):
    pass
print("some useful work")

#Questions on this lec.
#q1 (using while)       
n = int(input("n :-")) 
sum = 0
i = 1
while i <= n:
    sum += i
    i +=1
print("sum =", sum)    

#q2
#while loop 
n = int(input("n :-"))
fact = 1
i = 1 
while i <= n:
    fact *= i
    i += 1
    
print("factorial =", fact)                                                                                                                             
    
n = int(input("n :-"))
fact = 1

for i in range(1,n+1):
    fact *= i 
print("factorial = ", fact)

# end of lec.5                                                                                                                                                                                                                                                              