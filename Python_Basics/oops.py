"""
========================================== OOPs (object Oriented Programming )=====================================
-------------------------------------------------------------------------------------------------------------------
It is used to represents code more structured way.

In OOPS we have to create two things :-
------------------------------------------
1. class :- It is a blueprint for different objects.
    => class is combination of properties and methods 
     -> properties(attributes) :- These are variables declared inside the class.
     -> methods :- These are the funtions declared inside the class.

2. object :- It is an instance in place of that class.

NOTE :- we can create multiple objects on a single class.

In world there are so many programming languages that follow oops :-
--------------------------------------------------------------------
ex:- Python , C++ , JAVA , PHP , JS , R , etc...

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
syntax:-
---------
class className:
    properties
    methods

objectName = className()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*There are 4 pillers of OOPS that determines whether a language is object orietnted OR not :-
*--------------------------------------------------------------------------------------------
1. Inheritence
2. Polymorphism
3. Encapsulation
4. Abstraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

^1. Inheritence :- Using inheritence we can access properties and methods of another class to the current class.
During inheritence there are two types of classes ;-
1. Parent class
2. Child class

There are two types of Inheritence :-
--------------------------------------
1. Multiple Inheritence
2. Multi-level Inheritence
"""

class students:
    # these are properties(variables)
    name="Ram singh"
    age=21
    address ="mathura"

    # This is a Method
    def show_details(self):
        print(f"""
        =============== Students details ===================
              Name : {self.name}
              Age  : {self.age}
              Address : {self.address}
        =====================================================
        """)

# NOTE : In a class every method should have self paramter. Here self represents current class.

# here std1 is our Object
std1 = students()
# print(std1.name)
# std1.show_details()

#* ==================================== Inheritence ==============================================

class Parent1:
    parent_name="Parent1 Name"

    def parent_method1(self):
        print("This is Our parent1 method")

class Parent2:
    parent_name="Parent2 Name"

    def parent_method2(self):
        print("This is Our parent2 method")

# Multiple-Inheritence
class child(Parent1,Parent2):
    child_name="Child Name"

    def child_method(self):
        print("This is Clild Method")


child1 = child()
# child1.child_method()
# child1.parent_method1()
# child1.parent_method2()


# Multi-level Inheritence.
class A:
    def A(self):
        print("From A class")

class B(A):
    def B(self):
        print("From B class")

class C(B):
    def C(self):
        print("From C class")

class D(C):
    def D(self):
        print("From D class")

d = D()

# d.D()
# d.A()
# d.B()

#* ============================= Polymorphism ==============================
"""
polymorphism => poly(many) + morphism(shape) => many shapes
--------------------------------------------------------------------------------------
In different classes functions or properties names are same , but different behavior
--------------------------------------------------------------------------------------

"""

class cat:
    name = "cat"
    def sound(self):
        print("cat miow")

class dog:
    name="dog"
    def sound(self):
        print("Dog bhow")


# cat1 = cat()
# print(cat1.name)

# dog1 = dog()
# print(dog1.name)


#* ======================= Encapsulation ================================
# Binding properties aned methods inside the class and not allow direct access.
"""
OOPS Access Modifiers :-
-------------------------
There are three types of access modifiers :-
---------------------------------------------
1. public :- by default in a class every property and method is Publically accessable.
2. protected :- A variable or method start with single underscore(_)
NOTE :- Python does Not follow protected access modier. 
3. private :- A variable or method start with double underscore(__)
              Can only access inside the class OR using Inheritence.


ex:- In c++ 
------------
class employee{
    public char name[] = "Ram";
    private int salary = 20000;
}
"""

class employee:
    name = "Ram" # public access
    __salary = 20000
    _occupation = "manager"

    def show_details(self):
        print("Employee Salary is : ",self.__salary)
emp1 = employee()
# print(emp1.name)
# print(emp1._occupation)

# print(emp1.__salary) # AttributeError

# emp1.show_details()

#* ===================================== Abstraction ================================================
# Abstraction Mean HIDING.
"""
Abstraction means declare a method inside the class and it is mendatory to apply by 
that class which inherits the class.

syntax:- To apply abstraction we have to use ABC(Abstract Base Class) module.
---------
from abc import ABC,abstractmethod

# To make a class abstract class -

class className(ABC):
    properties 
    method1 

    @abstractmethod
    method2

"""
from abc import ABC , abstractmethod

class cbse(ABC):
    bord = "CBSE Board"
    def full_form(self):
        print("Full of CBSE is : Central Board Of Secondary Education")
    
    @abstractmethod
    def syllabus(self):
        pass

class schoolA(cbse):
    school_name = "ABC School"

    def school_info(self):
        print("""
        Name :- ABC School
        Location :- Mathura
        Medium :- English Medium 
        """)

    def syllabus(self):
        print("Our Syllabus is Affiliated to CBSE")

s1 = schoolA()
# s1.school_info()       
# s1.syllabus()
# s1.full_form()

#* =========================== constructor function in OOPS ==================================
# It is a function that calls automatically when we create  object of the class.
"""
syntax:-
--------
def __init__(self,parameter1,parameter2,..):
    statement
"""

class student(ABC):
    # constructor :- calls automatically when we create Object
    def __init__(self,school_name):
        self.school_name = school_name
        print(f"This student Studies in {school_name} School")

    def student_info(self,name,age,cls):
        # we have to declare these paremeters before use
        self.name=name
        self.age = age
        self.cls = cls
        print(f"""
        Name of student is : {name}
        Age of student is : {age}
        Class of student is : {cls}
        """)
    @abstractmethod
    def marks(self,mark):
        pass

class std(student):
    def __init__(self):
        print("hello")
    def marks(self,mark):
        self.mark = mark
        print("Marks")
        print(mark)
# st = student("Kanha makhan")
s1 = std()
s1.marks(89)
# st.student_info("Raman singh",17,"11th")
# std1.student_info("Suman singh",15,"10th")

#* ======================================== static method =========================================
# these are the methods that calls without creating object of the class
"""
syntax:-
----------

class className:
    def method1(self):
        statement
    
    @staticmethod
    def method2():
        statement

NOTE :- static methods are called using their className instead of creating its Object.
className.method2()
"""
class car :
    # constructor 
    def __init__(self):
        print("This car belongs to Tata")

    @staticmethod
    def car_start():
        print("Car Starts")

# car.car_start()


#* =========================== class method =========================================
# this method is also called without creating the object.

class phone:
    @classmethod
    def phone_functionalities(cls):
        print("Name : Samsung")
        print("Storage : 256GB")


# phone.phone_functionalities()

#* =============================== Magic Methods in OOPS =========================================
# These are the methods that starts and ends with double underscore Also called as Dunder Methods
# These are self calling methods, we do not have to call them explcitly.
"""
=> __init__(self) :- Constructor method
=> __del__(self) :- Destructor method
=> __str__(self)
=> __add__(self)
=> __sub__(self)
=> __gt__(self)
=> __lt__(self)
=> __ge__(self)
"""

class A:
    def __init__(self):
        print("Constructor Method")
    def sum(self,a,b):
        self.a=a
        self.b = b
        print("Sum is : ",a+b)

    def __del__(self):
        print("Destructor Method")

# a = A()
# a.sum(10,20)



class calculate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        print(f"Sum is : {self.x+other.x}, {self.y+other.y}") 

    def __sub__(self,other):
        print(f"Difference is : {self.x-other.x}, {self.y-other.y}") 

    def __mul__(self,other):
        print(f"multiplication is : {self.x*other.x}, {self.y*other.y}") 

    def __truediv__(self,other):
        print(f"Division is : {self.x/other.x}, {self.y/other.y}") 
        
s1 = calculate(10,120)
s2 = calculate(190,200)

# s1+s2
# s2-s1
# s2*s1
# s2/s1



class Student:
    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __gt__(self, other):
        return self.marks > other.marks

std1 = Student(89) 
std2 = Student(39)


print(std1==std2)