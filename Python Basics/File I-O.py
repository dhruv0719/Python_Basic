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
