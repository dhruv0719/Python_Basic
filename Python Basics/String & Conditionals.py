#lec 2 notes 

#strings
str1 = "Dhruv\n Enterpenure"
str2 = "Smart\t also"
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
str3 = "work in every phase of life"

#endswith function
print(str3.endswith("fe"))     #if yes then it shows True,if not then False.

#capitalize function 
print(str3.capitalize())
print(str3)    #this is not capitalize the main string, this will create the another string in with the first letter will be Captial.

str3 = str3.capitalize() 
print(str3)   #if we want to change in main function use this

#replace function
print(str3.replace("e", "s"))
print(str3.replace("life","Jivan"))

#find function
print(str3.find("f"))
print(str3.find("of"))
print(str3.find("e"))

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
w = int(input("write a number which you want :- "))

rem = w%7
 
if(rem == 0):
    print("yes this no. is multiple of 7")
else:
    print("this no. is not multiple of 7")
print("end of ques. no. 3")    
     
print("end of lec.2")    