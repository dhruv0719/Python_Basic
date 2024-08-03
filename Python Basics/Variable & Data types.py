#lec.no.1 notes 

print("Hello World")        #in this print is function 

print(23)
print(23+45)

#concept of varabile

name= "Dhruv"
age= 18
value= 99.69 
work = True
disrescept = None
print("our name is :", name)
print("oue age is : ", age)
print("our value is :", value)

# datatypes

print(type(name))        #string datatype
print(type(age))         #integers datatype
print(type(value))       #float datatype
print(type(work))        # boolean datatype
print(type(disrescept))  # none datatype

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
print(a%b)     #remainder
print(a**b)    #a^b 

#Relational/Comparion Operators
print(a==b)    #False
print(a!=b)    #True
print(a>=b)    #False
print(a>b)     #False
print(a<=b)    #True
print(a<b)     #True

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
sum = print("Sum of X & Y is",x+y)
print(sum)
#que.2
j=int(input("j : "))
print("area of square =", j * j)
#que.3
d = float(input("d: "))
s = float(input("s: "))
print("avg =",     (d+s)/2)


#end of lec.no.1