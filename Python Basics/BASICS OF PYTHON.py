#lec.no.1 notes 

print("Hello World")        #in this print is function 

print(23)
print(23+45)


#concept of varabile

name= "Dhruv and Sneha"
age= 20
value= 99.69 
work = True
disrescept = None
print("our name is :", name)
print("oue age is : ", age)
print("our value is :", value)

# datatypes

print(type(name))  #string datatype
print(type(age))     #integers datatype
print(type(value))     #float datatype
print(type(work))        # boolean datatype
print(type(disrescept))        # none datatype


#print sum             

a=2
b=6
sum = a + b
diff= a-b
print(sum)
print(diff)

#types of operators

#arithmetic operators
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)    #remainder
print(a**b)    #a^b 

#Relational/Comparion Operators
print(a==b)    #False
print(a!=b)    #True
print(a>=b)    #False
print(a>b)    #False
print(a<=b)    #True
print(a<b)    #True

#Assignment Operators
num = 10
num +=  10
print("num :", num) 
#and there are lost of this , for refercence accese pdf note

#logical operators
print(not a>b)
print(not a<b)

print("and operator:", (a==b) and (a<b))
print("and operator:", (a==b) and (a>b))

print("or operator:", (a==b) or (a>b))
print("or operator:", (a==b) or (a<b))


#Type conversion
q = 2
w = 4.69

e = int("9") 

print(type(e))
sum = q+w
summ = q+e
print(sum) 
print(summ)


#input form users 

name = input("enter your name :- ")
age = input("enter your age :- ")
print("welcome", name)
print("your age is", age)    

int("5")
val = int(input("enter some value: ")) 
print(type(val), val)

#practice of lec.no.1

#que.1
x = int(input("x : ")) 
y = int(input("y : "))
sum = x+y
print(sum)
#que.2
j=int(input("j : "))
print("area of square =", j * j)
#que.3
d = float(input("d: "))
s = float(input("s: "))
print("avg =",     (d+s)/2)

#end of lec.no.1 


#lec 2 notes 

#strings
str1 = "dil sneha\n sachme"
str2 = "dil dhruv\ti also"
print(str1)
print(str2)
print(str1 + " " + str2) #it is concatenation

print(len(str1))
print(len(str1 + "" + str2))

#indexing :- on string which letter was there
print(str1[:])

#slicing ( use in ML )
print(str2[0:12]) 
print(str1[:22])    #[0:22]
print(str2[12:])    #[12:len(str)]

#slicing :- negative index, is ka matlb hai ki string ko staring se nahi ending se count hoga
print(str1[-15:-3])
 
#String Function
str3 = "we stay toghter in every face of life"

#endswith function
print(str3.endswith("fe"))     #if yes then it shows True,if not then False.

#capitalize function 
print(str3.capitalize())
print(str3)    #this is not capitalize the main string, this will create the another string in with the first letter will be Captial.

str3 = str3.capitalize() 
print(str3)   #if we want to change in main function use this

#replace function
print(str3.replace("e", "s"))
print(str3.replace("toghter","Hamesha"))

#find function
print(str3.find("f"))
print(str3.find("stay"))
print(str3.find("z"))

#count function
print(str3.count("in"))

#question on this topic

#que1
name = input("Name :- ")
print("Lenght of your name is ", len(name))
#que2
str4="Hello everyone,$$how are$ you$ i hope$ that you are $earn very well in $ "
print("this '$' symbol in str4 how many thimes :- ",str4.count("$"))



#Conditional Statements
age  = 20

if(age>= 18):
    print("Can vote and applyed for licence")
    print("be safe when you drive")

light = input("what is color in signal :- ")
if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("Go")
elif(light == "yellow"):
        print("Look")
else:
    print("light is damge")

print("end of code")
    
num = 5
if(num>2):
    print("greater then 2")    #the space before print is know as "indentation" 
elif(num>3):
    print("greater then 3")
     
#example on conditional statements

marks = int(input("enter your marks :- "))
if(marks>=90):
    print("grade = A")
elif(marks>=80 and marks<90):
    print("grade = B")
elif(marks>=70 and marks<80):
    print("grade = C")
else:
    print("grade = D")


#concept of nesting

age = int(input("your age :-" ))

if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can dirve")
else:
    print("cannot drive")
    
#practice ques lec.2 

#que 1
num = int(input("enter number :- "))
                                                                                
rem = num%2                                                                                                                  
                                                                                                                                     
if(rem == 0):
    print("even")
else:
    print("odd")
    
print("end of ques.1")
                                                                                    
#qu 2.

a = int(input("enter 1st number :- "))
b = int(input("enter 2nd number :- "))
c = int(input("enter 3rd number :- "))

if(a>b and a>c):
    print("greatest number is =", a)
elif(b>c):
    print("greatest number is =", b)
else:
    print("greatest number is =", c)
    
print("end of ques. 2")

#ques. 3
w = int(input("write a number with you want :- "))

rem = w%7
 
if(rem == 0):
    print("yes this no. is multiple of 7")
else:
    print("this no. is not multiple of 7")
print("end of ques. no. 3")    
     
print("end of lec.2")    

# end of lec.2


#lec.3

#Lists in python

marks = [97.5,57.3,88.3,96.4,79.6]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[1])

student = ["Sneha",86,20,"navagam"]
print(student)

str = "hello"
print(str[0])
#str[0] = "y" :- this is not happen in string, but this is possible in list

student[0] = "Dhruv"
print(student)

#List slicing
print(marks[0:4])
print(marks[-3:-1])


#List Method
list = [2,1,3]
#append method = adds one element at the end 
list.append(4)
print(list)

#sort method = sorts is ascending order
print(list.sort())
print(list)

#for descending order 
print(list.sort(reverse=True))
print(list)

list1 = ["banana","apple","orange"]
print(list1.sort())
print(list1)

print(list1.sort(reverse=True))
print(list1)

#reverse Method
list1.reverse()
print(list1)

#insert method :- we want to add some value in list  
list1.insert(2,"mango")    #here 2 is index value of list 
print(list1)

#remove method :- remove element form occurrence of element  
list1.remove("apple")
print(list1)

#pop method :- remove element form given index
list1.pop(2)
print(list1)


#Tuples in python 

tup = (2,1,5,6,7)
print(type(tup))
print(tup[0])
print(tup[1])
#tup[0] = 3 ; this show the error like string. 

tup1 = ()
print(tup1)
print(type(tup))

tup2  = ("yoyo",)    #if we didin't give comma after the single world or number. then the python thinks that this is a intger or string, so it cann't consider as a tuple.
print(tup2)
print(type(tup2))

#Tuple Method 

#index method  
print(tup.index(6))
#count method 
print(tup.count(5))

#Practice Question

#ques1 
Movies = []

Movies.append(input("enter 1st movie : "))
Movies.append(input("enter 2nd movie : "))
Movies.append(input("enter 3rd movie : "))

print(Movies)

#ques2
list1 = [1,2,1]
list2 = [1,3,2]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 ==  list1):
    print("palindrome")
else:
    print("not palindrome")
    
copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome")
else:
    print("not palindrome")
    
#ques3
tup = ("C","D","A","A","B","B","A")
print(tup.count("A"))

#ques4
list = ["C","D","A","A","B","B","A"]
list.sort()
print(list)                                                        
                                                                                                               

#end of lec.no3


#lec 4 

#Dictionary of Python :- it is use to store data values in key:value pairs
dict = {
    "key" : "value",
    "name" : "Dhruv",    #"name" is know as key 
    "want" : "Enterpuner",
    "age" : 17,
    "is_adult" : False,
    "subject" : ["Maths","Python","Data"],
    "topic" : ("Dict","set"),
    "marks" : 69.96,
    12.8 : 98.8,
    11 : 23.33
}
#in keys we can't use dict and list, which mean in key we want that type of datatype which can't the value. if we want we will use tuples(but it is not use mant time) 

print(type(dict))
print(dict)

print(dict["want"])
print(dict["name"])

dict["name"] = "Sneha"
dict["age"] = 20
dict["is_adult"] = True

dict["surname"] = "Patil"
print(dict)

null_dict = {}
print(null_dict)
null_dict["name"] = "WOW"
print(null_dict)

#Nested Dictionary 

student = {
    "name" : "Sneha Bagul",
    "subjects" : {
        "phy" : 88,
        "chem" : 74,
        "math" : 69
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])

#Dictionary Methods

#key method
print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))
print(len(student))

#values method
print(student.values())
print(list(student.values()))

#items method
print(student.items())
print(list(student.items()))

pairs = list(student.items()) 
print(pairs[0])
print(pairs[1])

#get method
print(student["name"])
print(student.get("name"))
    #if we did this bymistake
      #      print(student["name1"])    # this will show error 
print(student.get("name1"))    # this can't show error this show "None"

#update method 
student.update({"city" : "surat", "lover" : "Dhruv"})
print(student)
                        
new_dict = {"city" : "surat", "lover" : "Dhruv"}
student.update(new_dict)
print(student)

                        
#Set in python = set is collection of the unordered items, the element must be unique & immutable(unchangeable); in this lists & dict are  not came because they are mutable 

# sets are mutable, but the element of sets is immutable. 

collection = {0,1,1,2,3,2,4,"Sneha","Dhruv"} #if we write one element more then one times then the sets will ingore that and doesn't show error  

print(collection)             
print(type(collection))
print(len(collection)) # in this also they ingore the repeted element/vlaue     

# empty set                                     
                                                
collection1 = {} # this is not a empty set this is a empty dictionary
print(collection1)            
collection2 = set()     #empty set
print(collection2)
print(type(collection2))

#Sets Method

#add method 
collection.add("love brid")
collection.add("Serious wala")
collection.add(69)
collection.add((2,3,4,5))
#collection.add([1,2,3])    :- this give a error of unhasable type list; just because in list we can the element, but is not valied for sets. 
print(collection)
print(len(collection))
#remove method
collection.remove(4)
print(collection)

#clear method
collection.clear()
print(collection)

#pop method 
collection3 = {"Sneha","Dhruv","are life partner","ofcoure the age are differnt and Sneha is 2 years big then Dhruv","but what will happen nothing"}
print(collection3)
print(collection3.pop())

#Union Method 
set1 = {1,2,3,4,5}
set2 = {9,8,7,6,3,2,1}

print(set1.union(set2))

print(set1)
print(set2)

#Intersection Method
print(set1.intersection(set2))


#Practice Questions 

#que1 
dict1 = {
                 "table" : ("a piece of furniture","list of facts & figures"),
                 "cat" : "a small animal"                
}
print(dict1)

#que2
subject = {
    "p","j","c++","p","js","j","p","j","c++","c"
}
print(len(subject))

#que3
dict1 = {}

dict1.update({"Physics" : input("Marks of Physics :- ", )})
dict1.update({"Chemistry" : input("Marks of Chemistry :- ", )})
dict1.update({"Maths" : input("Marks of Maths :- ", )})

print(dict1)

values = {9,"9.0"}    #if we can't make 9.0 in string form then the python consider 9 & 9.0 same, so we need to applyed that in string form
print(values)

#we can do this by in built datatype;
values1 = {
     ("float",9.0),
     ("int", 9)
}
print(values1)


#end of lec.4                                                                                                                                                 


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
                 
cal_fact(69)

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


#Lec.7
# File I/O in python

#Open,read & close File
f = open("demo.txt","r")    #"demo.txt" is a file in storage & 'r' is use for the mode of the file  
data = f.read()
print(data)
print(type(data))

f.close()

#Reading a file

f = open("demo.txt","r")    

data = f.read(5)        #here 5 shows the no. of character in that file (including space also)
print(data)
line1 = f.readline()    #so in this case we will only get that character with are not inculding on that read data which we are given in last line as a read
print(line1) 

f.close()

#for readline
f = open("demo.txt","r")    

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()    # we know that there was no line 3 in a file. so in this case we get a empty line. 
print(line3) 
f.close()

#Writing to a file
f = open("demo.txt","w")     #here mode - 'w' is known for write, this is overwrite. ; but old data was delete, when you write with "w"   

f.write("I want to become the more fouces person in this world. 143")

f.close()

f = open("demo.txt", "a") #here mode - 'a' is known as append, means add at the end ;in this old data of file is not delete. and whatever we are write that will add to file with out remove the current data of file  
f.write("\nThen i want Sneha in my life as my wife and lifeline. and she become everthing like my family. because i want her to jion me on my mission and my family")      

f.close()

#whenever we want to open a file in 'w' , 'a' mode. and the is not created there, then python will automaticlily created that file
f = open("sample.txt", "w")
f.close()

f = open("demo.txt", "r+")    #yaha per "r+" ko isliye use kiya hai q ki hum file ko read ke sath sath write bhi karna chahate hai. but yaha per hum jo bhi write karna chahate hai vo file me ki starting wali character ko gayab karega or wha per aapni jaha le kar, baki ke text ke sath judh jayega
f.write("abc")    #jesa hum ne dekha abhi kese ye work kiya yaha per
print(f.read())
f.close()    
  
f = open("demo.txt", "w+")    # w+ mode is use for reading and writing but in this case our file willl be truncated. truncated means the file is open in empty way. and whatever we want there to write we can write.     
print(f.read())
f.write("abc")    #this is write on file, old data was delete
f.close()    


f = open("demo.txt", "a+")    # a+ mode is use for reading and writing but in this case file will over write that thing after the present data on file..     
print(f.read())
f.write("Dhruv & Sneha")    #this is write on file, after the already data present in the file
f.close()

#summry of modes
""" r :- read mode = open for reading only. 
     w :- write mode = open for writing, but truncating the file first.
     a :- append mode = open for writing, appending to the end of the file if it exist, it                                                 will not truncated the file data.
     r+ :- read+ mode = overwrite (pointter is on starting). and no truncate,file data is                                                not deleted
      w+ :- write+ mode = overwrite. truncate, file data is deleted first
      a+ :- append+ mode = append. no truncate, data will not delete here, and new                                                            data was write on the end of the file data
"""
# with Syntax

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

with open("demo.txt", "w") as f:
    f.write("new data")

#Deleting a file

import os 

os.remove("sample.txt")    #now we can see that the file is deleted

#Practice Questions
#q1
with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")

#q2
with open("practice.txt","r") as f:
    data = f.read()                                                      

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt","w")  as f:
    f.write(new_data)
    
#q3
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("not found")       
#code as per the function
def check_for_word() :
    word = "xlearning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):    # "data.find(word) != -1" iski jaha per hum ye bhi likh sakte hai "word in data"
            print("Found")
        else:
            print("not found")

check_for_word()

#Q4
def check_for_line():
    word = "Sneha"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
            
    return -1

print(check_for_line())

#Q5
with open("practice1.txt", "r") as f:
    data = f.read()
    print(data)
#by simple way
num = ""
for i in range(len(data)):
    if(data[i] == ","):
        print(int(num))
        num = ""
    else:
        num += data[i]     

#by different way
count = 0
with open("practice1.txt", "r") as f:
    data = f.read()
    print(data)
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
        
        
print(count)

print("end of lec.7")

# end of lec 7

#lec8

#OOP in Python 

#Class & Object in Python
class Student:
    name = "Chaman"
    
s1 = Student ()
print(s1.name)   

s2 = Student()
print(s2.name)

class Car:
    color = "Black"
    brand = "BMW"      #line 1160,1161,1162 shows that how the class is created

car1 = Car()        #this show that how the object is created
print(car1.color)
print(car1.brand)

# __init__ function
#constructor :- All classes have a  function called __init__(), which is always executed when the object is being initiated. and it use with all the object with is present in class

class Student:            #if there was not a def __init__(), then python will automatically do that by it's defualt system 

#default constructors
    def __init__(self):
       pass
       
#parameterized constructors       
    def __init__(self, name,marks):     #if we didn't write self here that it will show a error,     here self is reference to the current instance of this class, and is used to access variable that belong to the class.
        self.name = name
        self.marks = marks
        print("adding new student in Database.")
        
s1 = Student ("Chaman",69)
print(s1.name, s1.marks) 

s2 = Student ("Chadani",96)
print(s2.name, s2.marks)

#Class & Instance Attributes :- class attr. is commom for all the obj. & instance attr. is for a single-single object  

class Student:
       college_name = "Chapara Institute of Technology" 
       name = "Chachi ji"        # this is known as class attr
       
       def __init__(self,name,marks):
        self.name = name     #obj attr > class attr
        self.marks = marks
        print("adding new student in Database.")
        
s1 = Student ("Chaman",69)
print(s1.name, s1.marks) 

#Method 

class Student:
    college_name = "Chapara Institute of Technology"
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def welcome(self):
        print("Welcome", self.name)
        
    def get_marks(self):
        return self.marks
        
                                                                                
s1 = Student("Chaman", 69)
s1.welcome()
print(s1.get_marks())

# practice 

class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
            
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your avg score is :- ", sum/3)    
                
s1 = Student("Tony Stark",[99,95,92])
s1.get_avg()

s1.name = "Ironman"     #in attr we can change the name , as we see here
s1.get_avg()

#Static method :- Method that don't use the self parameter (work at class level)

class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
        
    @staticmethod    #this is know as decorator :- it's work is to take a function and decorator that function and give that function
    def hello():
        print("hello") 
               
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your avg score is :- ", sum/3)    
                
s1 = Student("Tony Stark",[99,95,92])
s1.get_avg()
s1.hello()

s1.name = "Ironman"     
s1.get_avg()
s1.hello()

#Abstraction :- hiding the implementation details of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.acc = True       #there we can see that line 131&132 are unnesscary step. the are details is in a class 
        print("car started..")

car1 = Car()
car1.start() # here we write a code to start a car. then we see that the output is came is not like with is on line 131&132.    this is know as  Abstraction 

#Encapsulation :- Wrapping data and function into a single unit (object) 


#Question 

#Q1

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance = ", self.get_balance())
        
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())
        
    def get_balance(self):
        return self.balance  
                  
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)

#del keywork :- used to delete obj properties or obj itself

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Dhruv")
print(s1.name)
del s1.name
#print(s1.name)        #when we print a delete thing then system will show the error  


#Private(like) attr & method :- it's use for within class. not outside the class
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass    #here the two underscore ater the "self." and before the acc_pass , that is use to make the attr as privte 
    def reset_pass(self):
        print(self.__acc_pass)        
        
acc1 = Account("12345", "abcde")
print(acc1.acc_no)
#print(acc1.__acc_pass)         #as we known that we are keep the acc_pass as a private, if we try to print that then system will show the error to us. if we want to access the pass then we will do that from class only. that pass will not show outside the class 
print(acc1.reset_pass())

class Person:
    __name = "chachundhar"
    
    def __hello(self):
        print("hello person")
        
    def welcome(self):
         self.__hello()  

p1 = Person()
#print(p1.__name)       
#print(p1.__hello())
 #we put hastag here because we didn't want that the system will show the error. this show error because of the we are put that attr/method is private 
print(p1.welcome())    #here we know that the welcome function is not private, but as we know the welcome fun. is used the privite __hello . but techical it is right because the welcome and hello function are in same class.         so we can access only the welcome not hello       

 #Inheritance :- when one class(child/derived) derives the properties & method of another class(parent/base).
class Car:
   @staticmethod
   def start():
       print("car stated..")
       
   @staticmethod
   def stop():
       print("car stopped.")
       
class BmwCar(Car):
       def __init__(self, name):
           self.name = name       
       
car1 = BmwCar("X5")
car2 = BmwCar("G7")


# Types of inheritance :- ~Single Inheritance ; ~Multi-level Inheritance; ~Multiple Inheritance 

#upper code is the example of Single inheritance
#given below is a example of Multi-level inheritance
class Car:
   @staticmethod
   def start():
       print("car stated..")
       
   @staticmethod
   def stop():
       print("car stopped.")
       
class BmwCar(Car):
       def __init__(self, brand):
           self.name = brand       
       
class X7(BmwCar):
    def __init__(self, type):
        self.brand =  type

car1 = X7("petrol")
car1.start()

#example of multiple inheritance 
 
class A:
    varA = "welcome to class A"
    
class B:
    varB = "welcome to class B"
    
class C(A, B):
    varC = "welcome to class C"
    
c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)   

                                                  
# Super method                                                        
                                                                                    
class Car:
       def __init__(self, type):
           self.type = type
       @staticmethod
       def start():
           print("car stated..")
       
       @staticmethod
       def stop():
           print("car stopped.")
       
class BmwCar(Car):
       def __init__(self, name, type):
           self.name = name       
           super().__init__(type)    # if we didn`t used super method, then the program will show the error. if we use it then it wil not show us error
           super().start() 

car1 = BmwCar("X7", "electric")
print(car1.type)
                                                                                                                

# Class method :- 

class Person:
     name = "anonymous"
     
     def changeName(self, name):
         self.name = name                                #here self.name was created a new name. but we didn`t wan`t that we want the name is changeing in the class  
         
p1 = Person()
p1.changeName("Sneha Baugal")
print(p1.name)           
print(Person.name)
#by this simple method we can see that when we want to print a class name then the system will show as a old name with is present before when we edit a name in a class. 

#we try here to change the name with present in a class. we go to change that name through the obj. but can`t able to do it   

#to change the class name there are sucg way here

class Person:
     name = "anonymous"
     
     def changeName(self, name):
         Person.name = name           #to change name in class through the obj, u can do it like this way
         
p1 = Person()
p1.changeName("Sneha Baugal")
print(p1.name)           
print(Person.name)
  
#one more way 
class Person:
     name = "anonymous"
     
     def changeName(self, name):
         self.__class__.name = "Dhruv"
         
p1 = Person()
p1.changeName("Dhruv Patil")
print(p1.name)           
print(Person.name) 

class Person:
    name = "anonymous"
    
    @classmethod
    def changeName(cls, name):
        cls.name = name
        
p1 = Person()
p1.changeName("Dhruv Patil")
print(p1.name)
print(Person.name)


#Property

class Student:
    def __init__(self, phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
    def  calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"        

stu1 = Student(98,90,94)
print(stu1.percentage)

stu1.phy = 89
print(stu1.phy)
stu1.calcPercentage()
print(stu1.percentage)                     

#we can do this by the Property

class Student:
    def __init__(self, phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
             
    @property
    def percentage(self):
             return str((self.phy + self.chem + self.math) / 3) + "%"
             
stu1 = Student(98,90,94)
print(stu1.percentage)

stu1.phy = 89
print(stu1.percentage)                     

# Polymorphism :- when the same operator is allowed to have different meaning accordomh to the context

print(1+2)    #3
print(type(1))

print("apna" + "college")  #concatcnate
print(type("apna"))
print([1, 2, 3] + [4,5,6])  #merge
print(type([1,2,3]))    
        
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real,"i +", self.img, "j")
        
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)                                            
                                
num1 = Complex(1, 3)
num1.showNumber()                

num2 = Complex(6, 5)
num2.showNumber()                

num3 = num1 + num2
num3.showNumber()                                                  

# Question

#q1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
      
    def perimeter(self):
        return 2 * (22/7) * self.radius
        
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

#q2
"""class Employee:
    def __iniy__(self, role, dept, salary):
        self.role = role
        self.dept = depy
        self.salary = salary
      
    def showDetails(self):
        print("role =", self.role)                                                                         
        print("dept =" , self.depy)               
        print("salary =", self.salary)              
e1 = Employee("accountant", "Finance", "60,000")
e1.showDetails()                        
 """                      
                       
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
      
    def showDetails(self):
        print("role =", self.role)                                                                         
        print("dept =", self.dept)               
        print("salary =", self.salary)              
class Engnineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75000")

e1 = Employee("accountant", "Finance", "60,000")
e1.showDetails()     

engg1 = Engnineer("Elon Musk", 45)
engg1.showDetails()
              
#q3

class Order:
            def __init__(self, item, price):
                self.item = item                                                                                                                    
                self.price = price
                
            def __gt__(self, odr2):
                return self.price > odr2.price        # if we didn`t write this two line then there was error came
                                                                                                    
odr1 = Order("chips", 20)
odr2 = Order("tea", 15)

print(odr1 > odr2)  #true


#End                                                                                                                                                                                              