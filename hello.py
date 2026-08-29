#Python Fundamentals - 1
print("hello world")
print("hello world","with python")
print("hello \n world", "with python")

name = "Soniya"
age = 19
print("My name is: ",name)
print("My age is: ",age + 0.5)

#sum of 2 numbers
a = 10
b = 5
sum = a+b
print("The sum is: ", sum)

#airthmetic
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
#relational
print(a>b)
print(a<b)
print(a!=b)
print(a==b)
print(a>=b)
#assignment 
c = 10
c += 1 # c = c + 1 'similarly for other airthmetic operations'
print(c)
#logical
var = False
print(not var) # logical not
print((5>3) and (3>8)) # logical and
print((5>3) or (3>2)) # logical or

#user input
username = input("Enter your name: ")
print("Welcome", username)

#avg of 2 no's
a = float(input("Enter a: "))
b = float(input("Enter b: "))
avg = (a+b)/2
print("The average is: ",avg)


# Python Fundamentals - 2
age = 21 
if age >= 18:
    print("You can  vote")
else:
    print("You can't vote")

# Traffic lights 
color = input ("Enter color: ")
if color == "red":
    print("Stop")
elif color == "green":
    print("Go")
elif color == "yellow":
    print("Look")
else :
    print("Wrong color")

# Check whether a multiple or not
n = int(input("Enter num: "))
if (n % 5 == 0):
    print("multiple of 5")
else:
    print("not a multiple of 5")

# Nesting 
username = input("Enter username: ") 
password = input ("Enter password: ")
if (username == "admin" and password == "pass"):
    print("Success")
else:
    if (username != "admin"):
        print("Wrong username")
    else:
        print("Wrong password")

# Loops
count = 1
while (count <=5):
    print("Hello World")
    count += 1
print("after loop, count =", count)   

# Multiplication of any table
n = int(input("Enter number: "))
i = 1
while (i <= 10):
    print(n*i)
    i+=1

# Sum of n natural number
n = int(input("Enter number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("sum =", sum)

#Funtion
def sum (a,b): #fn def
    s = a+b
    return s
ans = sum (3,4) #fn call
print (ans)

#lambda fn
avg = lambda a,b: (a+b)/2
print(avg(4,5))

#factorial
def calc_fact(n):
    fact = 1
    for i in range (1, n+1):
        fact*=i
    return fact
n =int(input("Enter n: "))
print(calc_fact(n))

#list 
marks = [99,45,67,92,"abc",99.99]
print(marks[:])
print(marks[5:])
print(marks[:6])
print(marks[-5:-2])
 
#list methods (special type of functions)
nums = [1,2,3]
nums.append(4)
print(nums)
nums.insert(2,10)
print(nums)
nums.sort()
print(nums) #by default increasing
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)

#Linear search 
nums = [1,2,10,3,4]
x=10
idx=0
for val in nums:
    if(val==x):
        print(f"{x} found at idx = {idx}") #f strings formatting used 
        break
    idx+=1

#tuple
tup = (1,2,3,4,5)
print(tup)
print(type(tup))
print(len(tup))
print(tup[:])

tup = (1,)
print(type(tup))
tup1= ("abc") #single value tuple(,) else treats as expression
print(type(tup1))

#loop for sum 
tup = (1,2,3,4,5)
sum = 0
for val in tup:
    sum += val
print(f"sum of vals is {sum}")

#tup methods 
tup = (1,2,2,4,2,3)
print(tup.index(2))
print(tup.count(2))

#dictionary
info = {
    "name": "soniya", 
    "id": 25491,
    "age": 19,
    "subject": ["maths","cse"],
    2: "tday"
}
print(info)
print(type(info))
info["age"] = 19.5
print(info["age"])

#dict methods
dict_keys = info.keys()
print(dict_keys)
dict_vals = list(info.values())
print(dict_vals)
print(info.items())
print(info.get("id2")) #use of get gives none if wrong key
print("EOC") #no error in wrong key thus rest code gets executed
info.update({
    "city": "Rkt"
})
print(info)

#set
s = {1,2,2,2,3}
print(s)
print(type(s))
print(len(s))
s.add(5)
print(s)
empty_set = set() #constructor fn, {} make empty dict not set
s.remove(5)
s.pop()
s.clear()
print(s)
s1 = {1,2,3,4,5}
s2 = {4,5,8,9,10}
print(s1.union(s2))
print(s1.intersection(s2))