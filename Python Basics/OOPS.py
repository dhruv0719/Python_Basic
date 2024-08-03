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
    brand = "BMW"      #line 15,16,17 shows that how the class is created

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