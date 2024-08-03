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