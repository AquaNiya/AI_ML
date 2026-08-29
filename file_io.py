f= open ("sample.txt","r") #file object 
data = f.read()
print(data)
print(type(data))
f.close()

f1= open ("sample.txt","r") #file object 
data1 = f1.readline()
print(data1)
data1 = f1.readline()
print(data1)
f1.close()

f= open("sample.txt","w")
f.write("Text to overwrite \n the complete data :\n This is a sample file for demo of file I/O in Python programming language ")
f.close()

f= open("sample.txt","a")
f.write("\nNew text being appended\n to the file")
f.close()

with open ("sample.txt","r") as f:
    data = f.read()
    print(len(data))

#Word Search
data = True
line = 1
word = "Python"
with open("sample.txt","r") as f:
    while data:
        data = f.readline()
        if(word in data):
            print(f"{word} found at line {line}")
            break
        line += 1

#Exception handling with file I/O
try:
    x = int(input("Enter a number: "))
    ans = 100/x
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input, please enter a number")   
else:
    print(f"Answer is {ans}")
finally:
    print("This block will always execute") 
 
#List Comprehension
sq = [i*i for i in range (6)]  
print(sq) 

sq_odd = [i*i for i in range (6) if i%2!=0]   
print(sq_odd)

nums = [-2,-3,3,4,-1,7]
nums = [0 if val<0 else val for val in nums]
print(nums)

words = ["python","is","a","programming","language"]
print(words[0].upper())
words = [val.upper() for val in words]     
print(words)

#JSON MODULE
import json
json_str = '{"name": "Soniya","isTeacher": true}'
py_obj = json.loads(json_str)
print (type(json_str))
print (type(py_obj), py_obj)

import json
py_obj = {
    "name": "Soniya",
    "isTeacher": True
}
json_str = json.dumps(py_obj)
print(type(json_str), json_str)

import json
with open("data.json","r") as f:
    py_obj = json.load(f)
    print(type(py_obj), py_obj)

import json
data = {
    "name": "Soniya",
    "age": 20,
    "isTeacher": True
}
with open("data.json","w") as f:
    json.dump(data, f,indent=4,sort_keys=True)