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