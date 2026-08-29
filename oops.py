class Student:
    def __init__(self): #default constructor
        print("obj is being constructed")
    def __init__ (self, name , cgpa): #parameterized const 
        self.name = name
        self.cgpa = cgpa
    def get_cgpa(self):
        return self.cgpa
stu1 = Student("Rahul" , 9.0)
stu2 = Student("Urvashi" , 8.4)
stu3 = Student("Shradha" , 9.2)
print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")

class Student:
    college_name = "ABC college" #class
    PI = 3.1
    def __init__(self,name,gpa):
        self.name = name #instance
        self.gpa = gpa 
        self.PI = 3.14
stu1 = Student("Rahul", 9.0)
print(stu1.name)
print(stu1.college_name)
print(Student.college_name)
print(stu1.PI)
print(Student.PI)

class Laptop:
    storage_type = "SSD"
    def __init__(self , RAM , storage):
        self.RAM = RAM
        self.storage = storage
    @classmethod
    def get_storage_type(cls): #class method
        print(f"storage type = {cls.storage_type}")
    def get_info(self): #instance method 
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")
    @staticmethod
    def calc_discount(price,discount):
        final_price = price - (discount*price/100)
        print(f"discounted price = {final_price}")
l1 = Laptop("16gb","512gb" )
l2 = Laptop("8gb","256gb" )
l1.get_info()
l2.get_info()
Laptop.get_storage_type()
l2.get_storage_type() #can be called from the name of object and class name too 
#static method:- fnx => (price,discount) => final price(100 , 10) 
l1.calc_discount(40_000, 10)

#Product Store 
class product:
    count = 0 #class attr
    def __init__(self,name,price): #Instance attr
        self.name = name 
        self.price = price
        product.count += 1
    def get_info(self): #instance method
        print(f"price of {self.name} is Rs. {self.price}")
    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")
    @staticmethod
    def calc_discount(price, discount):
        print(f"discounted price = {price - (price * discount/ 100)}")
p1 = product("phone",10_000)
p2 = product("laptop",50_000)
p3 = product("pen",10)
p1.get_info() 
product.get_count()
p1.calc_discount(p1.price, 12)

#Encapsulation
class BankAccount:
    def __init__(self, name , balance):
        self.name = name #public
        self.__balance = balance #protected _ & __ private
    def get_balance(self): #getter
        return self.__balance   
    def set_balance(self,newBalance): #setter
        self.__balance = newBalance 

acc1 = BankAccount("Rahul Kumar", 100_000)
acc1.set_balance(200_000)
print(acc1.name , acc1.get_balance)
print(acc1.name , acc1._BankAccount__balance)

#Inheritance
class Employee:
    start_time = "10am"
    end_time = "6pm"
    def change_time(self,new_end_time):
        self.end_time = new_end_time
class Teacher(Employee):
    def __init__(self,subject):
        self.subject = subject
class AdminStaff(Employee):
    def __init__(self,role):
        self.role = role
t1 = Teacher("Math")
print(t1.subject,t1.start_time,t1.end_time)
t1.change_time("5pm")
staff1 = AdminStaff("Manager")  
print(staff1.role,staff1.start_time,staff1.end_time)

#MultiLevel Instance
class Employee:
    start_time = "10am"
    end_time = "6pm"
class AdminStaff(Employee):
    def __init__(self,role):
        self.role = role
class Accountant(AdminStaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary = salary
acc1 = Accountant(25_000,"CA")
print(acc1.role,acc1.salary,acc1.start_time,acc1.end_time)  

#Multiple Instance
class Teacher:
    def __init__(self,salary):
        self.salary = salary
class Student:
    def __init__(self,gpa):
        self.gpa = gpa
class TA(Teacher,Student):
    def __init__(self,salary,gpa,name):
        super().__init__(salary)
        Student.__init__(self,gpa)
        self.name = name
ta1 = TA(15_000,9.3,"Abc")
print(ta1.name,ta1.gpa,ta1.salary)

#Abstraction
from abc import ABC ,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass
class Lion(Animal):
    def make_sound(self):
        print("Roar")
class Cow(Animal):
    def make_sound(self):
        print("Moo!")
lion = Lion()
lion.make_sound() 
cow = Cow()
cow.make_sound()

#Polymorphism
#Function overriding 
class Employee:
    def get_designation(self):
        print("designation = Employee")
class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher")
t1 = Teacher()
t1.get_designation()
#Duck Typing
class Teacher():
    def get_designation(self):
        print("designation = Teacher")
class Accountant():
    def get_designation(self):
        print("designation = Accountant")
t1 = Teacher()
t1.get_designation()
acc1 = Accountant()
acc1.get_designation()

