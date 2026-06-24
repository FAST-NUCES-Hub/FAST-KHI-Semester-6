# ============================================================
# LAB 01
# ============================================================

print("Hello, World!")

# eval(input) accepts both int and float; input() always returns string
a = eval(input("Enter a number: "))
print(a)

# --- String Slicing ---
# Indexing starts at 0; end index is exclusive
uni = "FAST-NUCES"
print(uni[0:4])   # FAST
print(uni[:4])    # FAST
print(uni[5:])    # NUCES
print(uni[5:8])   # NUC
print(5 * "k")    # kkkkk  (string repetition)

# --- Variables ---
a = 2          # int
b = 3.3        # float
c = 'mehak'    # string

# --- Numeric Data Types ---
int_data     = 17
float_data   = 12.6
complex_data = 14 + 5j
print('Data:', int_data,     ', Type:', type(int_data))
print('Data:', float_data,   ', Type:', type(float_data))
print('Data:', complex_data, ', Type:', type(complex_data))

# --- String Operations ---
t = 'Hello World!'
print(t)          # complete string
print(t[0])       # first character
print(t[2:5])     # characters at index 2-4
print(t[2:])      # from index 2 onward
print(t * 2)      # string repeated twice
print(t + " TEST")

# --- Collection Data Types ---
list_data  = [11, 12, 13, 14, 15, 'orange']
tuple_data = (12, 15, 17, 'kiran')
set_data   = {'ali', 'hassan', 'ayesha', 12, 18.6}
range_data = range(1, 11)

# --- List Operations ---
list1 = ['physics', 'chemistry', 1997, 2000]
print("list1[0]:", list1[0])
list1[2] = 2001
del list1[2]
print("After modification:", list1)

# Nested list: [row][col]
lst = [[1, 2, 3], [4, 5, 6]]
print(lst[1][1])  # 5

# --- Dictionary ---
dc = {"name": "Abdullah", "course": ["AI", "CN"]}
print(dc["course"][0])

dc2 = {"name": {"f_name": "Abdullah", "l_name": "Yaqoob"}, "course": ["AI", "CN"]}
print(dc2["name"]["f_name"])

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

# --- User Input ---
# name = input("Enter your name: ")
# print(name)

# --- Conditional Statements ---
age = 18
if age >= 18:
    print("You are eligible to vote.")
elif age >= 16:
    print("Almost eligible.")
else:
    print("Not eligible to vote.")

# --- Loops ---
# For loop
for var in range(5):
    print(var)

for letter in 'Python':
    print('Current Letter:', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print('Current fruit:', fruit)

# While loop
count = 0
while count < 9:
    print('The count is:', count)
    count += 1
print('Good Bye')

# --- Functions ---
def non_para_func():
    print("This is Non-parametric Function")

def para_func(a, b):
    return a + b

def add(*args):
    return sum(args)

def details(name, age=13):           # default argument
    print('Name:', name, 'Age:', age)

def keyword_details(name, age, height):  # keyword argument
    print('Name:', name, 'Age:', age, 'Height:', height)

def variable_kw(**name):             # keyword variable length
    print('Names:', name)

non_para_func()
print(para_func(1, 2))
print(add(1, 2, 3, 4))
details('Mehak')
keyword_details(name='Ali', age=99, height=5.5)
variable_kw(n1='Mehak', n2='Ali', n3='Zainab')

# --- Math Module ---
import math
print("pi:", math.pi)
print("ceil(4.2):", math.ceil(4.2))
print("floor(4.8):", math.floor(4.8))
print("sqrt(16):", math.sqrt(16))
print("factorial(5):", math.factorial(5))
print("log(8,2):", math.log(8, 2))
print("sin(pi/2):", math.sin(math.pi / 2))
print("degrees(pi):", math.degrees(math.pi))

# --- Random Module ---
import random
print("random():", random.random())
print("randint(1,6):", random.randint(1, 6))
colors = ['red', 'blue', 'green', 'yellow']
print("choice:", random.choice(colors))
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print("shuffled:", nums)


# ============================================================
# LAB 02
# ============================================================

# --- 2.1 Class and Object ---
class MyClass:
    x = 5  # class attribute

    def method_one(self):
        print("This is method one")

m1 = MyClass()
print(m1.x)
m1.method_one()

# --- 2.2 Constructor (__init__) ---
class Student:
    school = "ABC High School"  # class attribute (shared by all)

    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age  = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, School: {Student.school}")

s1 = Student("Ali", 20)
s2 = Student("Sara", 22)
s1.display_info()
s2.display_info()

# Modifying attributes
s1.age = 21
Student.school = "XYZ School"
s1.display_info()
s2.display_info()

# --- Bank Account Example ---
class BankAccount:
    bank_name = "ABC Bank"

    def __init__(self, holder_name, account_no, balance):
        self.holder_name = holder_name
        self.account_no  = account_no
        self.balance     = balance

    def display_account(self):
        print(f"Bank: {BankAccount.bank_name} | Holder: {self.holder_name} "
              f"| Account: {self.account_no} | Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

account1 = BankAccount("Ali", 1001, 5000)
account2 = BankAccount("Sara", 1002, 7000)
account1.display_account()
account2.display_account()
account1.deposit(2000)

# --- Practice Task 1: Smart Light System ---
class SmartLight:
    def __init__(self, room_name):
        self.room_name = room_name
        self.status    = "OFF"

    def turn_on(self):
        self.status = "ON"
        print(f"{self.room_name} light turned ON.")

    def turn_off(self):
        self.status = "OFF"
        print(f"{self.room_name} light turned OFF.")

    def show_status(self):
        print(f"{self.room_name} light is {self.status}.")

light1 = SmartLight("Living Room")
light2 = SmartLight("Bedroom")
light1.turn_on()
light2.turn_off()
light1.show_status()
light2.show_status()

# --- 3. Inheritance ---
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child")

c = Child()
c.greet()        # inherited
c.greet_child()  # own method

# Inheritance with super()
class ParentSuper:
    def p(self):
        print("parent func")

class ChildSuper(ParentSuper):
    def p(self):
        print("child func")

    def c(self):
        self.p()       # calls child's p()
        super().p()    # calls parent's p()

co = ChildSuper()
co.c()

# Single Inheritance
class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def honk(self):
        print("Car honks")

car = Car()
car.move()
car.honk()

# Multiple Inheritance
class Parent1:
    def greet_p1(self): print("Hello from Parent1")

class Parent2:
    def greet_p2(self): print("Hello from Parent2")

class MultiChild(Parent1, Parent2):
    def greet_child(self): print("Hello from Child")

mc = MultiChild()
mc.greet_p1()
mc.greet_p2()
mc.greet_child()

# Multilevel Inheritance
class Grandparent:
    def greet_gp(self): print("Hello from Grandparent")

class ParentML(Grandparent):
    def greet_p(self): print("Hello from Parent")

class ChildML(ParentML):
    def greet_c(self): print("Hello from Child")

cml = ChildML()
cml.greet_gp()
cml.greet_p()
cml.greet_c()

# Hierarchical Inheritance
class HParent:
    def greet_parent(self): print("Hello from Parent")

class HChild1(HParent):
    def greet_c1(self): print("Hello from Child1")

class HChild2(HParent):
    def greet_c2(self): print("Hello from Child2")

c1, c2 = HChild1(), HChild2()
c1.greet_parent()
c1.greet_c1()
c2.greet_c2()

# Hybrid Inheritance
class HybridGP:
    def greet_gp(self): print("Hello from Grandparent")

class HybridP1(HybridGP):
    def greet_p1(self): print("Hello from Parent1")

class HybridP2:
    def greet_p2(self): print("Hello from Parent2")

class HybridChild(HybridP1, HybridP2):
    def greet_child(self): print("Hello from Child")

hc = HybridChild()
hc.greet_gp()
hc.greet_p1()
hc.greet_p2()
hc.greet_child()

# --- Practice Task 2: University Staff Management System ---
class Staff:
    def __init__(self, name, staff_id, department):
        self.name       = name
        self.staff_id   = staff_id
        self.department = department

    def display_info(self):
        print(f"Name: {self.name} | ID: {self.staff_id} | Dept: {self.department}")

class Teacher(Staff):
    def __init__(self, name, staff_id, department, courses, salary):
        super().__init__(name, staff_id, department)
        self.courses = courses
        self.salary  = salary

    def teach(self):
        print(f"{self.name} is teaching: {', '.join(self.courses)}")

    def display_info(self):
        super().display_info()
        print(f"  Courses: {self.courses} | Salary: {self.salary}")

class AdminStaff(Staff):
    def __init__(self, name, staff_id, department, role, working_hours):
        super().__init__(name, staff_id, department)
        self.role          = role
        self.working_hours = working_hours

    def perform_task(self):
        print(f"{self.name} ({self.role}) is performing administrative tasks.")

class ResearchAssistant(Staff):
    def __init__(self, name, staff_id, department, research_topic, stipend):
        super().__init__(name, staff_id, department)
        self.research_topic = research_topic
        self.stipend        = stipend

    def work_on_research(self):
        print(f"{self.name} is working on: {self.research_topic}")

t  = Teacher("Dr. Ali", "T01", "CS", ["AI", "ML"], 150000)
ad = AdminStaff("Sara", "A01", "Admin", "Registrar", 8)
ra = ResearchAssistant("Zaid", "R01", "CS", "Deep Learning", 25000)
t.display_info();  t.teach()
ad.display_info(); ad.perform_task()
ra.display_info(); ra.work_on_research()

# --- 4. Polymorphism ---

# Compile-Time (simulated via default args)
class Calculator:
    def add(self, a, b=0):
        print("Sum:", a + b)

calc = Calculator()
calc.add(5, 10)
calc.add(7)

# Compile-Time (simulated via *args)
class Calculator2:
    def add(self, *args):
        return sum(args)

calc2 = Calculator2()
print(calc2.add(5, 10))
print(calc2.add(5, 10, 15))

# Run-Time (Method Overriding)
class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

Dog().sound()
Cat().sound()

# --- 5. Encapsulation ---

# Public
class PubStudent:
    def __init__(self, name, roll_no):
        self.name    = name
        self.roll_no = roll_no

    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

ps = PubStudent("Ali", 101)
print(ps.name)
ps.display_info()

# Protected (single underscore)
class ProtStudent:
    def __init__(self, name, roll_no):
        self._name    = name
        self._roll_no = roll_no

    def _display_info(self):
        print(f"Name: {self._name}, Roll No: {self._roll_no}")

class ProtCollegeStudent(ProtStudent):
    def show(self):
        print(self._name)
        self._display_info()

pcs = ProtCollegeStudent("Sara", 102)
pcs.show()

# Private (double underscore)
class PrivStudent:
    def __init__(self, name, roll_no):
        self.__name    = name
        self.__roll_no = roll_no

    def __display_info(self):
        print(f"Name: {self.__name}, Roll No: {self.__roll_no}")

    def access_private(self):
        print("Accessing private members inside the class:")
        print(self.__name)
        self.__display_info()

sp = PrivStudent("Ali", 101)
sp.access_private()

# --- Practice Task 3: Bank Account (Encapsulation) ---
class SecureBankAccount:
    def __init__(self, holder_name, initial_balance=0):
        self.holder_name = holder_name
        self.__balance   = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Balance: {self.__balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

acc = SecureBankAccount("Ali", 5000)
acc.deposit(2000)
acc.withdraw(1000)
print("Balance:", acc.get_balance())

# ============================================================
# LAB 02 - POST-LAB TASKS
# ============================================================

# Task 1: AI Cybersecurity System (Inheritance)
class SecurityAgent:
    def __init__(self, agent_id, name, status="Active"):
        self.agent_id = agent_id
        self.name     = name
        self.status   = status

    def display_info(self):
        print(f"Agent ID: {self.agent_id} | Name: {self.name} | Status: {self.status}")

class FirewallAgent(SecurityAgent):
    def monitor_traffic(self):
        print(f"[{self.name}] Monitoring network traffic for threats...")

class MalwareDetectionAgent(SecurityAgent):
    def scan_files(self):
        print(f"[{self.name}] Scanning files for malware...")

class AutomationAgent(SecurityAgent):
    def run_automation(self):
        print(f"[{self.name}] Running AI-based automated security tasks...")

fa = FirewallAgent("AG01", "FirewallBot")
ma = MalwareDetectionAgent("AG02", "MalwareScanner")
aa = AutomationAgent("AG03", "AutoBot")
fa.display_info(); fa.monitor_traffic()
ma.display_info(); ma.scan_files()
aa.display_info(); aa.run_automation()

# Task 2: AI Threat Intelligence System (Inheritance)
class CyberThreat:
    def __init__(self, threat_id, name, severity):
        self.threat_id = threat_id
        self.name      = name
        self.severity  = severity

    def display_info(self):
        print(f"Threat: {self.name} | Severity: {self.severity}")

class PhishingThreat(CyberThreat):
    def analyze_email(self):
        print(f"[{self.name}] Analyzing suspicious email headers and links...")

class RansomwareThreat(CyberThreat):
    def scan_files(self):
        print(f"[{self.name}] Scanning file system for ransomware encryption patterns...")

class BotnetThreat(CyberThreat):
    def detect_traffic(self):
        print(f"[{self.name}] Detecting abnormal network traffic from botnet nodes...")

pt = PhishingThreat("T01", "PhishNet", "High")
rt = RansomwareThreat("T02", "CryptoLocker", "Critical")
bt = BotnetThreat("T03", "ZeroBot", "Medium")
pt.display_info(); pt.analyze_email()
rt.display_info(); rt.scan_files()
bt.display_info(); bt.detect_traffic()

# Task 3: AI Threat Response System (Polymorphism)
class ResponseAgent:
    def execute_response(self):
        print("Executing generic response...")

class AlertAgent(ResponseAgent):
    def execute_response(self):
        print("[AlertAgent] Sending notification alert to security team!")

class BlockAgent(ResponseAgent):
    def execute_response(self):
        print("[BlockAgent] Blocking malicious IP/process!")

class RecoverAgent(ResponseAgent):
    def execute_response(self):
        print("[RecoverAgent] Restoring affected systems from backup!")

agents = [AlertAgent(), BlockAgent(), RecoverAgent()]
for agent in agents:
    agent.execute_response()

# Task 4: Employee Management System (Polymorphism)
class Employee:
    def work(self):
        print("Employee is working.")

class Manager(Employee):
    def work(self):
        print("[Manager] Managing team and delegating tasks.")

class Developer(Employee):
    def work(self):
        print("[Developer] Writing and reviewing code.")

class Designer(Employee):
    def work(self):
        print("[Designer] Creating UI/UX designs.")

employees = [Manager(), Developer(), Designer()]
for emp in employees:
    emp.work()

# Task 5: Student Grading System (Encapsulation)
class GradedStudent:
    def __init__(self, name):
        self.name    = name
        self.__grade = None

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade. Must be 0-100.")

    def get_grade(self):
        return self.__grade

    def display_info(self):
        print(f"Student: {self.name} | Grade: {self.__grade}")

gs = GradedStudent("Ali")
gs.set_grade(85)
print("Grade:", gs.get_grade())
gs.display_info()
gs.set_grade(105)   # invalid


# ============================================================
# LAB 03
# ============================================================

import random

# --- Agent-Environment Interaction Pattern ---
# Every agent system needs three components:
#   1. Environment  – external world with state
#   2. Agent        – decision-making entity
#   3. Agent Program – internal logic (act method)

# Generic single-step agent runner
def run_agent(agent, environment):
    percept = environment.get_percept()
    action  = agent.act(percept)
    print(f"Percept: {percept}, Action: {action}")

# ============================================================
# 3.1 SIMPLE REFLEX AGENT
# Acts solely on the current percept (no memory)
# ============================================================

# Example 1: Hand-Pulling Agent
class HeatEnvironment:
    def __init__(self, heat_level='High'):
        self.heat_level = heat_level

    def get_percept(self):
        return 'Hot' if self.heat_level == 'High' else 'Cool'

class HandPullingAgent:
    def act(self, percept):
        if percept == 'Hot':
            return 'Pull hand away – you touched the hot object'
        return 'No need to pull away'

env   = HeatEnvironment(heat_level='High')
agent = HandPullingAgent()
run_agent(agent, env)

# Example 2: Vacuum Cleaner (1D)
class RoomEnvironment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'

class VacuumReflexAgent:
    def act(self, percept):
        if percept == 'Dirty':
            return 'Clean the room'
        return 'Room is already clean'

# Run vacuum agent for a fixed number of steps
def run_vacuum(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action  = agent.act(percept)
        print(f"Step {step+1}: Percept - {percept}, Action - {action}")
        if percept == 'Dirty':
            environment.clean_room()

run_vacuum(VacuumReflexAgent(), RoomEnvironment(), 5)

# Practice Task 1A: Random initial state
class RandomRoomEnv:
    def __init__(self):
        self.state = random.choice(['Dirty', 'Clean'])

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'

# Practice Task 1B: State changes randomly after each step
class DynamicRoomEnv:
    def __init__(self):
        self.state = random.choice(['Dirty', 'Clean'])

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'

    def random_dirty(self):
        self.state = random.choice(['Dirty', 'Clean'])

# Run vacuum agent in a dynamically dirtying environment
def run_dynamic_vacuum(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action  = agent.act(percept)
        print(f"Step {step+1}: Percept - {percept}, Action - {action}")
        if percept == 'Dirty':
            environment.clean_room()
        environment.random_dirty()

run_dynamic_vacuum(VacuumReflexAgent(), DynamicRoomEnv(), 5)

# Example 3: 2D Grid-Based Vacuum Cleaner (Smart Cleaning Robot)
# Grid: a(0) b(1) c(2) / d(3) e(4) f(5) / g(6) h(7) i(8)
class GridEnvironment:
    def __init__(self):
        self.grid = ['Clean', 'Dirty', 'Clean',
                     'Clean', 'Dirty', 'Dirty',
                     'Clean', 'Clean', 'Clean']

    def get_percept(self, position):
        return self.grid[position]

    def clean_room(self, position):
        self.grid[position] = 'Clean'

    def display_grid(self, agent_position):
        print("\nCurrent Grid State:")
        grid_display = self.grid[:]
        grid_display[agent_position] = "🤖"
        for i in range(0, 9, 3):
            print(" | ".join(grid_display[i:i+3]))
        print()

class GridVacuumAgent:
    def __init__(self):
        self.position = 0  # starts at 'a'

    def act(self, percept, grid):
        if percept == 'Dirty':
            grid[self.position] = 'Clean'
            return 'Clean the room'
        return 'Room is clean'

    def move(self):
        if self.position < 8:
            self.position += 1
        return self.position

# Run a grid-traversal agent for a fixed number of steps
def run_grid_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept(agent.position)
        action  = agent.act(percept, environment.grid)
        print(f"Step {step+1}: Position {agent.position} -> "
              f"Percept - {percept}, Action - {action}")
        environment.display_grid(agent.position)
        if percept == 'Dirty':
            environment.clean_room(agent.position)
        agent.move()

run_grid_agent(GridVacuumAgent(), GridEnvironment(), 9)

# ============================================================
# 3.2 MODEL-BASED AGENT
# Maintains an internal model of the world
# ============================================================

# Example 1: Vacuum Cleaner (Model-Based)
class ModelBasedVacuumAgent:
    def __init__(self):
        self.model = {}

    def update_model(self, percept):
        self.model['current'] = percept
        print(self.model)

    def predict_action(self):
        if self.model['current'] == 'Dirty':
            return 'Clean the room'
        return 'Room is clean'

    def act(self, percept):
        self.update_model(percept)
        return self.predict_action()

# Run a model-based agent and print each step
def run_model_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action  = agent.act(percept)
        print(f"Step {step+1}: Percept - {percept}, Action - {action}")
        if percept == 'Dirty':
            environment.clean_room()

run_model_agent(ModelBasedVacuumAgent(), RoomEnvironment(), 5)

# Example 2: Closing Windows When It Rains
class RainEnvironment:
    def __init__(self, rain='No', windows_open='Open'):
        self.rain         = rain
        self.windows_open = windows_open

    def get_percept(self):
        return {'rain': self.rain, 'windows_open': self.windows_open}

    def close_windows(self):
        if self.windows_open == 'Open':
            self.windows_open = 'Closed'

class WindowModelAgent:
    def __init__(self):
        self.model = {'rain': 'No', 'windows_open': 'Open'}

    def act(self, percept):
        self.model.update(percept)
        if self.model['rain'] == 'Yes' and self.model['windows_open'] == 'Open':
            return 'Close the windows'
        return 'No action needed'

# Run rain-detection agent; closes windows when raining
def run_rain_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action  = agent.act(percept)
        print(f"Step {step+1}: Percept - {percept}, Action - {action}")
        if action == 'Close the windows':
            environment.close_windows()

run_rain_agent(WindowModelAgent(), RainEnvironment(rain='Yes', windows_open='Open'), 5)

# ============================================================
# 3.3 GOAL-BASED AGENT
# Maintains a goal and plans actions to achieve it
# ============================================================

class GoalBasedVacuumAgent:
    def __init__(self):
        self.goal = 'Clean'

    def formulate_goal(self, percept):
        if percept == 'Dirty':
            self.goal = 'Clean'
        else:
            self.goal = 'No action needed'

    def act(self, percept):
        self.formulate_goal(percept)
        if self.goal == 'Clean':
            return 'Clean the room'
        return 'Room is clean'

# Run goal-based vacuum agent for a fixed number of steps
def run_goal_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action  = agent.act(percept)
        print(f"Step {step+1}: Percept - {percept}, Action - {action}")
        if percept == 'Dirty':
            environment.clean_room()

run_goal_agent(GoalBasedVacuumAgent(), RoomEnvironment(), 5)

# ============================================================
# 3.4 UTILITY-BASED AGENT
# Selects actions that maximise a utility function
# ============================================================

# Example 1: Vacuum Cleaner (Utility-Based)
class UtilityVacuumAgent:
    def __init__(self):
        self.utility = {'Dirty': -10, 'Clean': 10}

    def calculate_utility(self, percept):
        return self.utility[percept]

    def select_action(self, percept):
        if percept == 'Dirty':
            return 'Clean the room'
        return 'No action needed'

    def act(self, percept):
        return self.select_action(percept)

# Run utility-based agent; accumulates and prints total utility
def run_utility_agent(agent, environment, steps):
    total_utility = 0
    for step in range(steps):
        percept = environment.get_percept()
        action  = agent.act(percept)
        utility = agent.calculate_utility(percept)
        print(f"Step {step+1}: Percept - {percept}, Action - {action}, "
              f"Utility - {utility}")
        total_utility += utility
        if percept == 'Dirty':
            environment.clean_room()
    print("Total Utility:", total_utility)

run_utility_agent(UtilityVacuumAgent(), RoomEnvironment(), 5)

# Example 2: Choosing a Movie to Watch
class MovieEnvironment:
    def __init__(self, movies):
        self.movies = movies

    def get_percept(self):
        return self.movies

class UtilityMovieAgent:
    def __init__(self, mood_factor=0.7):
        self.mood_factor = mood_factor

    def utility(self, review):
        return review * self.mood_factor

    def act(self, percept):
        best_movie   = None
        best_utility = -float('inf')
        for movie, review in percept.items():
            mu = self.utility(review)
            if mu > best_utility:
                best_movie   = movie
                best_utility = mu
        return best_movie

# Run the movie-recommendation agent and print the best choice
def run_movie_agent(agent, environment):
    percept     = environment.get_percept()
    best_choice = agent.act(percept)
    print(f"Available Movies: {percept}")
    print(f"Best Movie to Watch: {best_choice}")

run_movie_agent(UtilityMovieAgent(mood_factor=0.8),
                MovieEnvironment({'Movie A': 7, 'Movie B': 9, 'Movie C': 5}))

# ============================================================
# 3.5 LEARNING-BASED AGENT (Q-Learning)
# Improves performance via feedback
# ============================================================

class LearningBasedAgent:
    def __init__(self, actions):
        self.Q       = {}
        self.actions = actions
        self.alpha   = 0.1   # learning rate
        self.gamma   = 0.9   # discount factor
        self.epsilon = 0.1   # exploration rate

    def get_Q_value(self, state, action):
        return self.Q.get((state, action), 0.0)

    def select_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)
        return max(self.actions, key=lambda a: self.get_Q_value(state, a))

    def learn(self, state, action, reward, next_state):
        old_Q        = self.get_Q_value(state, action)
        best_future  = max(self.get_Q_value(next_state, a) for a in self.actions)
        self.Q[(state, action)] = (old_Q +
                                   self.alpha * (reward + self.gamma * best_future - old_Q))

    def act(self, state):
        return self.select_action(state)

class LearningRoomEnv:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'
        return 10

    def no_action_reward(self):
        return 0

# Run learning agent; updates Q-values after each step
def run_learning_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action  = agent.act(percept)
        if percept == 'Dirty':
            reward = environment.clean_room()
        else:
            reward = environment.no_action_reward()
        print(f"Step {step+1}: Percept - {percept}, Action - {action}, "
              f"Reward - {reward}")
        next_percept = environment.get_percept()
        agent.learn(percept, action, reward, next_percept)

run_learning_agent(
    LearningBasedAgent(['Clean the room', 'No action needed']),
    LearningRoomEnv(), 5
)

# ============================================================
# LAB 03 - LAB TASKS
# ============================================================

# Task 1: Cybersecurity – 9-Component System (Simple Reflex Agent)
class CyberEnvironment:
    def __init__(self):
        self.components = {chr(65 + i): random.choice(['Safe', 'Vulnerable'])
                           for i in range(9)}

    def display(self):
        print("\nSystem State:")
        for comp, state in self.components.items():
            print(f"  Component {comp}: {state}")

class CyberSecurityAgent:
    def scan(self, components):
        vulnerabilities = []
        for comp, state in components.items():
            if state == 'Vulnerable':
                print(f"  [WARNING] Component {comp} is VULNERABLE!")
                vulnerabilities.append(comp)
            else:
                print(f"  [OK]      Component {comp} is Safe.")
        return vulnerabilities

    def patch(self, components, vulnerabilities):
        for comp in vulnerabilities:
            components[comp] = 'Safe'
            print(f"  [PATCHED] Component {comp} is now Safe.")

cyber_env   = CyberEnvironment()
cyber_agent = CyberSecurityAgent()
print("=== Initial System Check ===")
cyber_env.display()
print("\n=== System Scan ===")
vulns = cyber_agent.scan(cyber_env.components)
print("\n=== Patching Vulnerabilities ===")
cyber_agent.patch(cyber_env.components, vulns)
print("\n=== Final System Check ===")
cyber_env.display()

# Task 2: Load Balancer Agent (Model-Based)
class ServerEnvironment:
    def __init__(self):
        self.servers = {f"Server{i+1}": random.choice(['Underloaded', 'Balanced', 'Overloaded'])
                        for i in range(5)}

    def display(self):
        for server, load in self.servers.items():
            print(f"  {server}: {load}")

class LoadBalancerAgent:
    def balance(self, servers):
        overloaded   = [s for s, l in servers.items() if l == 'Overloaded']
        underloaded  = [s for s, l in servers.items() if l == 'Underloaded']
        for ol in overloaded:
            if underloaded:
                ul = underloaded.pop(0)
                print(f"  Moving task from {ol} to {ul}")
                servers[ol] = 'Balanced'
                servers[ul] = 'Balanced'

sv_env  = ServerEnvironment()
lb_agent = LoadBalancerAgent()
print("=== Initial Load ===")
sv_env.display()
lb_agent.balance(sv_env.servers)
print("\n=== After Balancing ===")
sv_env.display()

# Task 3: Backup Management Agent
backup_tasks = {f"Backup{i+1}": random.choice(['Completed', 'Failed'])
                for i in range(7)}
print("\n=== Backup Status Before ===")
for k, v in backup_tasks.items(): print(f"  {k}: {v}")

for task, status in backup_tasks.items():
    if status == 'Failed':
        print(f"  Retrying {task}...")
        backup_tasks[task] = 'Completed'

print("\n=== Backup Status After ===")
for k, v in backup_tasks.items(): print(f"  {k}: {v}")

# Task 4: Utility-Based Security Agent (Low/High Risk)
class UtilitySecurityEnv:
    def __init__(self):
        self.components = {chr(65 + i): random.choice(['Safe', 'Low Risk', 'High Risk'])
                           for i in range(9)}

class UtilitySecurityAgent:
    def scan_and_patch(self, components):
        for comp, state in components.items():
            if state == 'Safe':
                print(f"  [OK]       Component {comp}: Safe")
            elif state == 'Low Risk':
                print(f"  [PATCHING] Component {comp}: Low Risk -> patching...")
                components[comp] = 'Safe'
            else:
                print(f"  [ALERT]    Component {comp}: HIGH RISK – premium service needed!")

use_env   = UtilitySecurityEnv()
use_agent = UtilitySecurityAgent()
print("\n=== Utility Security Agent ===")
use_agent.scan_and_patch(use_env.components)
print("\n=== Final State ===")
for c, s in use_env.components.items(): print(f"  {c}: {s}")

# Task 5: Hospital Delivery Robot (Goal-Based Agent)
class HospitalEnvironment:
    def __init__(self):
        self.deliveries = [
            {'room': 'Room 101', 'patient_id': 'P001', 'medicine': 'Paracetamol', 'time': '08:00'},
            {'room': 'Room 205', 'patient_id': 'P002', 'medicine': 'Amoxicillin',  'time': '09:30'},
        ]
        self.storage_location = 'Medicine Storage'
        self.current_location = 'Charging Station'

class HospitalRobotAgent:
    def __init__(self):
        self.carrying = None

    def move_to(self, location):
        print(f"  Moving to: {location}")

    def pick_up_medicine(self, medicine, storage):
        self.move_to(storage)
        self.carrying = medicine
        print(f"  Picked up: {medicine}")

    def scan_patient(self, patient_id):
        print(f"  Scanning patient ID: {patient_id} ... Verified!")

    def deliver(self, room):
        self.move_to(room)
        print(f"  Delivered {self.carrying} to {room}")
        self.carrying = None

    def execute_deliveries(self, env):
        for d in env.deliveries:
            print(f"\n--- Delivery: {d['medicine']} to {d['room']} at {d['time']} ---")
            self.pick_up_medicine(d['medicine'], env.storage_location)
            self.scan_patient(d['patient_id'])
            self.deliver(d['room'])
        print("\nAll deliveries completed!")

h_env   = HospitalEnvironment()
h_robot = HospitalRobotAgent()
h_robot.execute_deliveries(h_env)

# Task 6: Firefighting Robot (3x3 Grid)
class FireEnvironment:
    def __init__(self):
        self.rooms = {
            'a': 'safe', 'b': 'safe', 'c': 'fire',
            'd': 'safe', 'e': 'fire', 'f': 'safe',
            'g': 'safe', 'h': 'safe', 'j': 'fire'
        }
        self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']

    def display(self, current=None):
        order = list(self.rooms.keys())
        print()
        for i in range(0, 9, 3):
            row = ""
            for room in order[i:i+3]:
                if room == current:
                    row += " 🤖"
                elif self.rooms[room] == 'fire':
                    row += " 🔥"
                else:
                    row += "  ."
            print(row)

class FireRobot:
    def move_and_extinguish(self, env):
        for room in env.path:
            print(f"\nRobot moves to room '{room}'")
            if env.rooms[room] == 'fire':
                print(f"  🔥 Fire detected! Extinguishing...")
                env.rooms[room] = 'safe'
                print(f"  ✅ Fire extinguished in room '{room}'")
            else:
                print(f"  Room '{room}' is safe.")
            env.display(current=room)
        print("\n✅ All fires extinguished!")

fire_env   = FireEnvironment()
fire_robot = FireRobot()
fire_robot.move_and_extinguish(fire_env)


# ============================================================
# LAB 04
# ============================================================

from collections import deque

# Common graph used in examples
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

# ============================================================
# 4.1 BREADTH-FIRST SEARCH (BFS)
# Explores level-by-level; uses a queue (FIFO)
# Guaranteed to find shortest path in unweighted graphs
# ============================================================

def bfs(graph, start, goal):
    visited = []
    queue   = []
    visited.append(start)
    queue.append(start)
    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        if node == goal:
            print("\nGoal found!")
            return
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print("\nGoal not found.")

print("BFS:")
bfs(tree, 'A', 'I')

# BFS Goal-Based Agent
class BFSGoalAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    def bfs_search(self, graph, start, goal):
        visited = []
        queue   = [start]
        visited.append(start)
        while queue:
            node = queue.pop(0)
            print(f"Visiting: {node}")
            if node == goal:
                return f"Goal {goal} found!"
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return "Goal not found"

    def act(self, percept, graph):
        status = self.formulate_goal(percept)
        if status == "Goal reached":
            return f"Goal {self.goal} found!"
        return self.bfs_search(graph, percept, self.goal)

class GraphEnvironment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

# Run BFS goal-based agent from a start node
def run_bfs_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action  = agent.act(percept, environment.graph)
    print(action)

bfs_agent = BFSGoalAgent('I')
graph_env = GraphEnvironment(tree)
print("\nBFS Goal-Based Agent:")
run_bfs_agent(bfs_agent, graph_env, 'A')

# ============================================================
# 4.2 DEPTH-FIRST SEARCH (DFS)
# Explores as deep as possible before backtracking; uses stack
# ============================================================

def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    print(start, end=' ')
    if start == goal:
        print("\nGoal found!")
        return True
    for neighbour in graph[start]:
        if neighbour not in visited:
            if dfs(graph, neighbour, goal, visited):
                return True
    return False

print("\nDFS:")
dfs(tree, 'A', 'I')

# ============================================================
# 4.3 DEPTH-LIMITED SEARCH (DLS)
# DFS with a maximum depth cutoff
# ============================================================

def dls(graph, start, goal, depth_limit):
    visited = []

    def dfs_limited(node, depth):
        if depth > depth_limit:
            return None
        visited.append(node)
        if node == goal:
            print(f"Goal found with DLS. Path: {visited}")
            return visited[:]
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                path = dfs_limited(neighbor, depth + 1)
                if path:
                    return path
        visited.pop()
        return None

    result = dfs_limited(start, 0)
    if not result:
        print("Goal not found within depth limit.")

print("\nDLS (depth=3):")
dls(tree, 'A', 'I', 3)

# DLS as Goal-Based Agent
class DLSGoalAgent:
    def __init__(self, goal, depth_limit):
        self.goal        = goal
        self.depth_limit = depth_limit

    def dls_search(self, graph, node, depth, visited):
        if depth > self.depth_limit:
            return None
        visited.append(node)
        if node == self.goal:
            return visited[:]
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                path = self.dls_search(graph, neighbor, depth + 1, visited)
                if path:
                    return path
        visited.pop()
        return None

    def act(self, graph, start):
        path = self.dls_search(graph, start, 0, [])
        if path:
            print(f"DLS Agent: Goal {self.goal} found! Path: {path}")
        else:
            print(f"DLS Agent: Goal not found within depth {self.depth_limit}")

dls_agent = DLSGoalAgent('I', depth_limit=4)
dls_agent.act(tree, 'A')

# ============================================================
# 4.4 ITERATIVE DEEPENING SEARCH (IDS)
# Combines DFS (memory) and BFS (completeness)
# ============================================================

def ids(graph, start, goal, max_depth):
    def dls_ids(node, goal, depth, path):
        if depth == 0:
            return False
        if node == goal:
            path.append(node)
            return True
        if node not in graph:
            return False
        for child in graph[node]:
            if dls_ids(child, goal, depth - 1, path):
                path.append(node)
                return True
        return False

    for depth in range(max_depth + 1):
        path = []
        if dls_ids(start, goal, depth, path):
            print(f"IDS Path (depth {depth}):", " -> ".join(reversed(path)))
            return
    print("Goal not found within max depth.")

print("\nIDS:")
ids(tree, 'A', 'I', 5)

# ============================================================
# 4.5 UNIFORM COST SEARCH (UCS)
# Expands lowest-cost node first; finds optimal path
# ============================================================

import heapq

weighted_graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

def ucs(graph, start, goal):
    frontier     = [(0, start)]
    visited      = set()
    cost_so_far  = {start: 0}
    came_from    = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_cost, current_node = frontier.pop(0)
        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == goal:
            path = []
            node = current_node
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            print(f"UCS Goal found. Path: {path}, Total Cost: {current_cost}")
            return
        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor]   = current_node
                frontier.append((new_cost, neighbor))
    print("Goal not found.")

print("\nUCS:")
ucs(weighted_graph, 'A', 'I')

# UCS Verbose (with frontier display)
def ucs_verbose(graph, start, goal):
    frontier    = [(0, start)]
    came_from   = {start: None}
    cost_so_far = {start: 0}
    visited     = []

    while frontier:
        print(f"Frontier: {frontier}")
        cost, current_node = heapq.heappop(frontier)
        print(f"Current: {current_node} | Cost: {cost}")
        if current_node in visited:
            continue
        visited.append(current_node)
        if current_node == goal:
            path    = []
            current = goal
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            print(f"\nGoal '{goal}' found!")
            print(f"Path: {' -> '.join(path)}")
            print(f"Total Cost: {cost}")
            return
        for neighbor, cost_value in graph[current_node].items():
            new_cost = cost + cost_value
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor]   = current_node
                heapq.heappush(frontier, (new_cost, neighbor))
    print("No path found.")

print("\nUCS Verbose:")
ucs_verbose(weighted_graph, 'A', 'I')

# UCS as Utility-Based Agent
class UCSUtilityAgent:
    def __init__(self, goal):
        self.goal = goal

    def act(self, graph, start):
        frontier    = [(0, start)]
        came_from   = {start: None}
        cost_so_far = {start: 0}
        visited     = set()

        while frontier:
            cost, node = heapq.heappop(frontier)
            if node in visited:
                continue
            visited.add(node)
            if node == self.goal:
                path    = []
                current = self.goal
                while current is not None:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                print(f"UCS Agent: Path={path}, Cost={cost}")
                return
            for neighbor, edge_cost in graph[node].items():
                new_cost = cost + edge_cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor]   = node
                    heapq.heappush(frontier, (new_cost, neighbor))
        print("UCS Agent: Goal not found.")

UCSUtilityAgent('I').act(weighted_graph, 'A')

# Maze via Goal-Based DFS Agent
class MazeEnvironment:
    def __init__(self, grid):
        self.grid  = grid
        self.rows  = len(grid)
        self.cols  = len(grid[0])
        self.start = self._find("S")
        self.goal  = self._find("G")

    def _find(self, target):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == target:
                    return (r, c)

    def get_view(self, pos):
        r, c = pos
        nbrs = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < self.rows and 0 <= nc < self.cols
                    and self.grid[nr][nc] != "#"):
                nbrs.append((nr, nc))
        return {"pos": pos, "nbrs": nbrs}

    def display(self, path):
        for r in range(self.rows):
            row = ""
            for c in range(self.cols):
                if self.grid[r][c] in ("S", "G"):
                    row += self.grid[r][c] + " "
                elif (r, c) in path:
                    row += "* "
                else:
                    row += self.grid[r][c] + " "
            print(row)

class MazeDFSAgent:
    def __init__(self, goal):
        self.goal      = goal
        self.seen      = []
        self.stack     = []
        self.came_from = {}

    def act(self, view):
        pos = view["pos"]
        self.seen.append(pos)
        print(f"Visiting: {pos}")
        if pos == self.goal:
            return "DONE"
        for nbr in reversed(view["nbrs"]):
            if nbr not in self.seen and nbr not in self.stack:
                self.stack.append(nbr)
                self.came_from[nbr] = pos
        return "MOVE"

    def get_path(self, end):
        path    = []
        current = end
        while current in self.came_from:
            path.append(current)
            current = self.came_from[current]
        path.append(current)
        path.reverse()
        return path

# Drive the DFS maze agent until goal or exhausted
def run_maze_agent(agent, env):
    agent.stack.append(env.start)
    agent.came_from[env.start] = None
    while agent.stack:
        pos = agent.stack.pop()
        if pos in agent.seen:
            continue
        view   = env.get_view(pos)
        action = agent.act(view)
        if action == "DONE":
            path = agent.get_path(env.goal)
            print(f"\nGoal {env.goal} reached!")
            print(f"Path: {path}")
            print(f"Steps: {len(path) - 1}\n")
            env.display(path)
            return
    print("No path found.")

maze_grid = [
    ["S", ".", "#", ".", "."],
    [".", ".", "#", ".", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", "#", "#", ".", "."],
    [".", ".", ".", "#", "G"],
]
maze_env   = MazeEnvironment(maze_grid)
maze_agent = MazeDFSAgent(maze_env.goal)
run_maze_agent(maze_agent, maze_env)

# ── BFS Maze ─────────────────────────────────
def bfs_maze(maze, start, goal):
    """BFS on a 2D grid. 0=open, 1=wall."""
    visited    = set([start])
    queue      = [start]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while queue:
        row, col = queue.pop(0)
        print("Visiting:", (row, col), end=" ")
        if (row, col) == goal:
            print("\nGoal found!")
            return True
        for dr, dc in directions:
            nr, nc = row+dr, col+dc
            if (0<=nr<len(maze) and 0<=nc<len(maze[0])
                    and maze[nr][nc]==0 and (nr,nc) not in visited):
                visited.add((nr,nc))
                queue.append((nr,nc))
    print("\nGoal not found.")
    return False

# ── DFS Maze ─────────────────────────────────
def dfs_maze(maze, start, goal):
    """DFS on a 2D grid. 0=open, 1=wall."""
    visited    = set([start])
    stack      = [start]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while stack:
        row, col = stack.pop()
        print("Visiting:", (row, col), end=" ")
        if (row, col) == goal:
            print("\nGoal found!")
            return True
        for dr, dc in directions:
            nr, nc = row+dr, col+dc
            if (0<=nr<len(maze) and 0<=nc<len(maze[0])
                    and maze[nr][nc]==0 and (nr,nc) not in visited):
                visited.add((nr,nc))
                stack.append((nr,nc))
    print("\nGoal not found.")
    return False

# ── DLS Maze ─────────────────────────────────
def dls_maze(maze, start, goal, depth_limit):
    """Depth-Limited Search on a 2D grid."""
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    visited    = set()

    def helper(row, col, depth):
        if depth > depth_limit:
            return None
        if (row, col) in visited:
            return None
        visited.add((row, col))
        print("Visiting:", (row, col), end=" ")
        if (row, col) == goal:
            return [(row, col)]
        for dr, dc in directions:
            nr, nc = row+dr, col+dc
            if (0<=nr<len(maze) and 0<=nc<len(maze[0]) and maze[nr][nc]==0):
                result = helper(nr, nc, depth+1)
                if result is not None:
                    return [(row, col)] + result
        visited.remove((row, col))
        return None

    result = helper(start[0], start[1], 0)
    if result:
        print(f"\nGoal found! Path: {result}")
    else:
        print("\nGoal not found.")
    return result

# ── IDFS Maze ────────────────────────────────
def idfs_maze(maze, start, goal, max_depth):
    """Iterative Deepening DFS on a 2D grid."""
    for depth in range(max_depth + 1):
        print(f"\n  [IDFS] Trying depth limit: {depth}")
        result = dls_maze(maze, start, goal, depth)
        if result:
            return result
    print("IDFS Maze: Goal not found.")
    return None

# ── Greedy BFS Maze ──────────────────────────
def greedy_bfs_maze(maze, start, goal):
    """Greedy Best-First Search on a 2D grid using Manhattan heuristic."""
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    frontier   = [(manhattan(start, goal), start)]
    visited    = set()
    came_from  = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[0])
        _, current = frontier.pop(0)
        if current in visited:
            continue
        visited.add(current)
        print("Visiting:", current, end=" ")
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            print(f"\nGoal found! Path: {path}")
            return path
        row, col = current
        for dr, dc in directions:
            nr, nc   = row+dr, col+dc
            neighbor = (nr, nc)
            if (0<=nr<len(maze) and 0<=nc<len(maze[0])
                    and maze[nr][nc]==0 and neighbor not in visited):
                came_from[neighbor] = current
                frontier.append((manhattan(neighbor, goal), neighbor))
    print("\nGoal not found.")
    return None

# ── Maze demo ────────────────────────────────
_demo_maze = [[0,0,1,0],[0,0,0,0],[0,1,1,0],[0,0,0,0]]
print("\nBFS Maze:")  ; bfs_maze(_demo_maze, (0,0), (3,3))
print("\nDFS Maze:")  ; dfs_maze(_demo_maze, (0,0), (3,3))
print("\nDLS Maze (limit=8):")  ; dls_maze(_demo_maze, (0,0), (3,3), 8)
print("\nIDFS Maze (max=8):")   ; idfs_maze(_demo_maze, (0,0), (3,3), 8)
print("\nGreedy BFS Maze:")     ; greedy_bfs_maze(_demo_maze, (0,0), (3,3))

# ============================================================
# LAB 04 - LAB TASKS
# ============================================================

# ── Task 1: DLS as Goal-Based Agent ──────────────────────────
class DLSAgent:
    def __init__(self, goal, depth_limit):
        self.goal        = goal
        self.depth_limit = depth_limit

    def dls(self, graph, node, depth, visited):
        if depth > self.depth_limit:
            return None
        visited.append(node)
        if node == self.goal:
            return visited[:]
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                result = self.dls(graph, neighbor, depth + 1, visited)
                if result:
                    return result
        visited.pop()
        return None

    def act(self, graph, start):
        result = self.dls(graph, start, 0, [])
        if result:
            print(f"DLS Goal-Based Agent: Path = {result}")
        else:
            print("DLS Goal-Based Agent: Goal not found within depth limit.")

DLSAgent('I', 4).act(tree, 'A')

# ── Task 1b: UCS as Utility-Based Agent ──────────────────────
UCSUtilityAgent('I').act(weighted_graph, 'A')

# ── Task 2: Travelling Salesman Problem (brute-force / DFS) ──
from itertools import permutations

tsp_distances = {
    1: {2: 10, 3: 15, 4: 20},
    2: {1: 10, 3: 35, 4: 25},
    3: {1: 15, 2: 35, 4: 30},
    4: {1: 20, 2: 25, 3: 30},
}

# Try all city permutations; return shortest round-trip
def tsp_brute_force(distances, start=1):
    cities    = [c for c in distances if c != start]
    best_path = None
    best_cost = float('inf')

    for perm in permutations(cities):
        path = [start] + list(perm) + [start]
        cost = sum(distances[path[i]][path[i+1]] for i in range(len(path) - 1))
        if cost < best_cost:
            best_cost = cost
            best_path = path

    print(f"TSP Best Path: {best_path}, Cost: {best_cost}")

tsp_brute_force(tsp_distances, start=1)

# ── Task 3: UCS for cheapest path ────────────────────────────
ucs(weighted_graph, 'A', 'I')

# ── Task 4: DLS for 8-Puzzle ─────────────────────────────────
def dls_8puzzle(start, goal, depth_limit):
    def get_neighbors_puzzle(state):
        neighbors = []
        idx       = state.index(0)
        row, col  = idx // 3, idx % 3
        moves     = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in moves:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_state      = list(state)
                new_idx        = nr * 3 + nc
                new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
                neighbors.append(tuple(new_state))
        return neighbors

    def dls_puzzle(state, depth, visited):
        if state == goal:
            return [state]
        if depth == 0:
            return None
        visited.add(state)
        for neighbor in get_neighbors_puzzle(state):
            if neighbor not in visited:
                result = dls_puzzle(neighbor, depth - 1, visited)
                if result:
                    return [state] + result
        visited.discard(state)
        return None

    result = dls_puzzle(tuple(start), depth_limit, set())
    if result:
        print(f"8-Puzzle DLS: Solution found in {len(result)-1} moves")
    else:
        print(f"8-Puzzle DLS: No solution within depth {depth_limit}")

puzzle_start = [1, 2, 3, 4, 0, 5, 6, 7, 8]
puzzle_goal  = (1, 2, 3, 4, 5, 6, 7, 8, 0)
dls_8puzzle(puzzle_start, puzzle_goal, depth_limit=10)

# ── Task 5: IDFS for decision-making ─────────────────────────
def idfs_decision(start, goal, max_depth):
    def dls_dec(node, depth, path, constraints):
        if node == goal:
            return path + [node]
        if depth == 0:
            return None
        new_constraints = [c for c in constraints if c != node]
        for child in decision_graph.get(node, []):
            if child not in path and child not in new_constraints:
                result = dls_dec(child, depth - 1, path + [node], new_constraints)
                if result:
                    return result
        return None

    decision_graph = {
        'Start': ['TaskA', 'TaskB'],
        'TaskA': ['TaskC', 'TaskD'],
        'TaskB': ['TaskD', 'TaskE'],
        'TaskC': ['Goal'],
        'TaskD': ['Goal'],
        'TaskE': [],
        'Goal':  []
    }

    for depth in range(max_depth + 1):
        result = dls_dec(start, depth, [], [])
        if result:
            print(f"IDFS Decision Path (depth {depth}): {result}")
            return
    print("IDFS: Goal not found.")

idfs_decision('Start', 'Goal', 6)

# ── Task 6: DFS Sudoku Solver with Constraint Propagation ────
def solve_sudoku(board):
    def is_valid(board, row, col, num):
        if num in board[row]:
            return False
        if num in [board[r][col] for r in range(9)]:
            return False
        br, bc = (row // 3) * 3, (col // 3) * 3
        for r in range(br, br + 3):
            for c in range(bc, bc + 3):
                if board[r][c] == num:
                    return False
        return True

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
if solve_sudoku(sudoku_board):
    print("Sudoku Solved:")
    for row in sudoku_board:
        print(row)


# ============================================================
# LAB 05
# ============================================================

# Informed search uses problem-specific knowledge (heuristics)
# to guide the search, reducing unnecessary exploration.
# Key concept: heuristic function h(n) estimates cost to goal.

from queue import PriorityQueue

# ============================================================
# 5.1 BEST-FIRST SEARCH
# Uses priority queue ordered by h(n); explores most promising nodes
# ============================================================

bfs_informed_graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [], 'E': [], 'F': [], 'G': [], 'J': [], 'K': [], 'L': [], 'M': []
}

def best_first_search(graph, start, goal):
    visited = set()
    pq      = PriorityQueue()
    pq.put((0, start))      # (heuristic, node)

    while not pq.empty():
        cost, node = pq.get()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            if node == goal:
                print("\nGoal reached!")
                return True
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    pq.put((weight, neighbor))

    print("\nGoal not reachable!")
    return False

print("Best-First Search:")
best_first_search(bfs_informed_graph, 'S', 'K')

# Maze using Best-First Search (Manhattan distance heuristic)
class MazeNode:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent   = parent
        self.g = 0    # cost from start
        self.h = 0    # heuristic (Manhattan)
        self.f = 0    # total (for BFS f=h; for A* f=g+h)

    def __lt__(self, other):
        return self.f < other.f

# ── Heuristic distance functions ─────────────────────────────
# Manhattan: sum of absolute axis differences (grid, 4-connected)
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Euclidean: straight-line distance between two grid cells
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Diagonal (Chebyshev): max of axis differences (8-connected grid)
def diagonal_distance(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return max(dx, dy)

# Best-First Search on a 2-D maze grid using Manhattan heuristic
def maze_best_first(maze, start, end):
    rows, cols  = len(maze), len(maze[0])
    start_node  = MazeNode(start)
    frontier    = PriorityQueue()
    frontier.put(start_node)
    visited     = set()

    while not frontier.empty():
        current     = frontier.get()
        current_pos = current.position

        if current_pos == end:
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        visited.add(current_pos)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            if (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols
                    and maze[new_pos[0]][new_pos[1]] == 0
                    and new_pos not in visited):
                new_node   = MazeNode(new_pos, current)
                new_node.h = manhattan(new_pos, end)
                new_node.f = new_node.h   # Best-First: f(n) = h(n)
                frontier.put(new_node)
                visited.add(new_pos)

    return None

maze_grid_bfs = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]
path = maze_best_first(maze_grid_bfs, (0, 0), (4, 4))
print("Maze Best-First Search Path:", path if path else "No path found")

# ============================================================
# 5.2 GREEDY BEST-FIRST SEARCH (GBFS)
# Like BFS but uses ONLY h(n); ignores actual cost g(n)
# Fast but not guaranteed optimal; can get stuck in loops
# f(n) = h(n)
# ============================================================

gbfs_graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}
heuristic_gbfs = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 7,
                  'F': 3, 'G': 6, 'H': 2, 'I': 0}

def greedy_bfs(graph, start, goal):
    frontier  = [(start, heuristic_gbfs[start])]
    visited   = set()
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, _ = frontier.pop(0)

        if current_node in visited:
            continue

        print(current_node, end=' ')
        visited.add(current_node)

        if current_node == goal:
            path = []
            node = current_node
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            print(f"\nGoal found with GBFS. Path: {path}")
            return

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                came_from[neighbor] = current_node
                frontier.append((neighbor, heuristic_gbfs[neighbor]))

    print("\nGoal not found")

print("\nGreedy Best-First Search:")
greedy_bfs(gbfs_graph, 'A', 'I')

# Difference: BFS uses f(n) which can include g(n) + h(n),
# Greedy BFS uses ONLY h(n), ignoring actual path cost.

# ============================================================
# 5.3 A* SEARCH
# Combines UCS (g(n)) and Greedy BFS (h(n))
# Evaluation: f(n) = g(n) + h(n)
# Optimal and complete when h(n) is admissible (never overestimates)
# ============================================================

astar_graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {},
}
heuristic_astar = {'A': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11, 'G': 0}

def a_star(graph, start, goal):
    frontier  = [(start, 0 + heuristic_astar[start])]
    visited   = set()
    g_costs   = {start: 0}
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, current_f = frontier.pop(0)

        if current_node in visited:
            continue

        print(current_node, end=' ')
        visited.add(current_node)

        if current_node == goal:
            path = []
            node = current_node
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            print(f"\nGoal found with A*. Path: {path}")
            return

        for neighbor, cost in graph[current_node].items():
            new_g  = g_costs[current_node] + cost
            f_cost = new_g + heuristic_astar[neighbor]
            if neighbor not in g_costs or new_g < g_costs[neighbor]:
                g_costs[neighbor]   = new_g
                came_from[neighbor] = current_node
                frontier.append((neighbor, f_cost))

    print("\nGoal not found")

print("\nA* Search:")
a_star(astar_graph, 'A', 'G')

# ============================================================
# LAB 05 - LAB TASKS
# ============================================================

# ── Task 1: Ambulance Navigation – Greedy BFS and A* ─────────
ambulance_graph = {
    'Hospital': {},
    'A':  {'B': 4,  'C': 3,  'Hospital': 10},
    'B':  {'E': 12, 'F': 5,  'Hospital': 8},
    'C':  {'D': 7,  'E': 10},
    'D':  {'E': 2},
    'E':  {'Hospital': 5},
    'F':  {'Hospital': 16},
}
ambulance_heuristic = {'A': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4,
                       'F': 11, 'Hospital': 0}
TRAFFIC_THRESHOLD   = 8   # roads with cost > threshold are delayed

# Simple Reflex Agent: avoids roads with traffic delay > threshold
class SimpleReflexAmbulanceAgent:
    def __init__(self, threshold):
        self.threshold = threshold

    def filter_neighbors(self, graph, node):
        return {nb: cost for nb, cost in graph[node].items()
                if cost <= self.threshold}

# Goal-Based Agent: replans if a road is blocked
class GoalBasedAmbulanceAgent:
    def __init__(self, goal):
        self.goal    = goal
        self.blocked = set()

    def block_road(self, from_node, to_node):
        self.blocked.add((from_node, to_node))
        print(f"  [REPLANNING] Road {from_node}->{to_node} blocked!")

    def a_star_plan(self, graph, start):
        heuristic = ambulance_heuristic
        frontier  = [(start, heuristic[start])]
        g_costs   = {start: 0}
        came_from = {start: None}
        visited   = set()
        while frontier:
            frontier.sort(key=lambda x: x[1])
            node, _ = frontier.pop(0)
            if node in visited:
                continue
            visited.add(node)
            if node == self.goal:
                path, n = [], node
                while n:
                    path.append(n)
                    n = came_from[n]
                return list(reversed(path)), g_costs[self.goal]
            for nb, cost in graph.get(node, {}).items():
                if (node, nb) in self.blocked:
                    continue
                ng = g_costs[node] + cost
                if nb not in g_costs or ng < g_costs[nb]:
                    g_costs[nb]   = ng
                    came_from[nb] = node
                    frontier.append((nb, ng + heuristic.get(nb, 0)))
        return None, float('inf')

# Run both algorithms
reflex_agent = SimpleReflexAmbulanceAgent(TRAFFIC_THRESHOLD)
goal_agent   = GoalBasedAmbulanceAgent('Hospital')
goal_agent.block_road('B', 'Hospital')    # simulate blockage

path, cost = goal_agent.a_star_plan(ambulance_graph, 'A')
print(f"\nAmbulance A* Path: {path}, Cost: {cost}")

# ── Task 2: Delivery Drone – Learning Heuristic ──────────────
drone_graph = {
    'Depot':    {'A': 4, 'B': 3},
    'A':        {'C': 7, 'D': 5},
    'B':        {'D': 10, 'E': 3},
    'C':        {'Target': 5},
    'D':        {'Target': 2},
    'E':        {'Target': 16},
    'Target':   {}
}
drone_heuristic = {'Depot': 14, 'A': 10, 'B': 9, 'C': 5, 'D': 2, 'E': 11, 'Target': 0}

# A* for the drone graph with a caller-supplied heuristic dict
def a_star_drone(graph, heuristic, start, goal):
    frontier  = [(start, heuristic[start])]
    g_costs   = {start: 0}
    came_from = {start: None}
    visited   = set()
    while frontier:
        frontier.sort(key=lambda x: x[1])
        node, _ = frontier.pop(0)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            path, n = [], node
            while n:
                path.append(n)
                n = came_from[n]
            return list(reversed(path)), g_costs[goal]
        for nb, cost in graph[node].items():
            ng = g_costs[node] + cost
            if nb not in g_costs or ng < g_costs[nb]:
                g_costs[nb]   = ng
                came_from[nb] = node
                frontier.append((nb, ng + heuristic.get(nb, 0)))
    return None, float('inf')

# Update heuristic from observed path cost (learning agent)
def update_heuristic(heuristic, path, actual_cost):
    segment_cost = actual_cost / max(len(path) - 1, 1)
    for i, node in enumerate(reversed(path)):
        heuristic[node] = max(heuristic[node], segment_cost * i)

path1, cost1 = a_star_drone(drone_graph, drone_heuristic, 'Depot', 'Target')
print(f"\nDrone Run 1: {path1}, Cost: {cost1}")
update_heuristic(drone_heuristic, path1, cost1)
path2, cost2 = a_star_drone(drone_graph, drone_heuristic, 'Depot', 'Target')
print(f"Drone Run 2 (learned): {path2}, Cost: {cost2}")

# ── Task 3: Flood Evacuation – Reflex Agent, Greedy BFS & A* ─
evacuation_graph = {
    'Start':    {'A': 4, 'B': 3},
    'A':        {'C': 7, 'SafeZone': 10},
    'B':        {'D': 10, 'SafeZone': 3},
    'C':        {'SafeZone': 5},
    'D':        {'SafeZone': 2},
    'SafeZone': {}
}
evac_heuristic = {'Start': 10, 'A': 7, 'B': 5, 'C': 3, 'D': 2, 'SafeZone': 0}
flooded_roads  = {('A', 'SafeZone')}   # dynamically blocked

class ReflexEvacAgent:
    def __init__(self, flooded):
        self.flooded = flooded

    def is_passable(self, from_node, to_node):
        if (from_node, to_node) in self.flooded:
            print(f"  [REFLEX] {from_node}->{to_node} is flooded! Avoiding.")
            return False
        return True

    def greedy_bfs(self, graph, start, goal):
        frontier  = [(start, evac_heuristic[start])]
        came_from = {start: None}
        visited   = set()
        while frontier:
            frontier.sort(key=lambda x: x[1])
            node, _ = frontier.pop(0)
            if node in visited:
                continue
            visited.add(node)
            if node == goal:
                path, n = [], node
                while n:
                    path.append(n)
                    n = came_from[n]
                return list(reversed(path))
            for nb in graph.get(node, {}):
                if nb not in visited and self.is_passable(node, nb):
                    came_from[nb] = node
                    frontier.append((nb, evac_heuristic.get(nb, 0)))
        return None

evac_agent = ReflexEvacAgent(flooded_roads)
evac_path  = evac_agent.greedy_bfs(evacuation_graph, 'Start', 'SafeZone')
print(f"\nEvacuation Path (GBFS + Reflex): {evac_path}")


# ============================================================
# LAB 06
# ============================================================

# Local search works on complete-state formulations:
# starts with a full candidate and improves it iteratively.
# Unlike systematic search, it does NOT track the path taken.


# ============================================================
# 6.3 GENETIC ALGORITHM (GA)
# Population-based: mimics natural selection
# Steps: Initialise → Evaluate fitness → Select → Crossover → Mutate → Repeat
# ============================================================

# ── GA for 8-Queens ──────────────────────────────────────────
# Chromosome: list of column positions (index = row)
# Maximum fitness = 28 (all 8 queens non-attacking)

N = 8  # board size

# Count non-attacking queen pairs; return 28 - conflicts
def fitness(chromosome):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if chromosome[i] == chromosome[j]:                         # same row
                conflicts += 1
            if abs(chromosome[i] - chromosome[j]) == abs(i - j):      # diagonal
                conflicts += 1
    return 28 - conflicts

# Generate a random 8-queens chromosome
def create_chromosome():
    return [random.randint(1, N) for _ in range(N)]

# Truncation selection: return top-2 by fitness
def selection(population):
    return sorted(population, key=fitness, reverse=True)[:2]

# Single-point crossover at a random cut point
def crossover(p1, p2):
    point = random.randint(1, N - 2)
    return p1[:point] + p2[point:]

# Random-reset mutation at one locus
def mutation(chromosome):
    idx              = random.randint(0, N - 1)
    chromosome[idx]  = random.randint(1, N)
    return chromosome

# Full GA loop for 8-Queens
def genetic_algorithm_8queens():
    population_size = 100
    generations     = 1000
    population      = [create_chromosome() for _ in range(population_size)]

    for generation in range(generations):
        for individual in population:
            if fitness(individual) == 28:
                print(f"\n8-Queens GA: Solution found at gen {generation}: {individual}")
                return individual

        p1, p2         = selection(population)
        new_population = []
        for _ in range(population_size):
            child = crossover(p1, p2)
            if random.random() < 0.1:
                child = mutation(child)
            new_population.append(child)
        population = new_population

    best = max(population, key=fitness)
    print(f"\n8-Queens GA: Best found: {best}, Fitness: {fitness(best)}")
    return best

genetic_algorithm_8queens()

# ── GA for N-Queens (alternative: fitness = –conflicts) ──────
# Negative conflicts so higher value = fewer conflicts
def ga_fitness_nq(state):
    return -calculate_conflicts(state)

# Full GA loop for N-Queens (generalised)
def ga_nqueens(n=8, pop_size=100, max_gen=1000, mutation_rate=0.1):
    population = [[random.randint(0, n - 1) for _ in range(n)] for _ in range(pop_size)]

    for generation in range(max_gen):
        best = max(population, key=ga_fitness_nq)
        if calculate_conflicts(best) == 0:
            print(f"GA N-Queens solved at gen {generation}: {best}")
            return best, 0

        scored  = sorted(population, key=ga_fitness_nq, reverse=True)
        parents = scored[:pop_size // 2]

        new_pop = []
        while len(new_pop) < pop_size:
            p1, p2 = random.sample(parents, 2)
            pt     = random.randint(0, n - 1)
            child  = p1[:pt] + p2[pt:]
            if random.random() < mutation_rate:
                child[random.randint(0, n - 1)] = random.randint(0, n - 1)
            new_pop.append(child)
        population = new_pop

    best = max(population, key=ga_fitness_nq)
    print(f"GA N-Queens best: {best}, Conflicts: {calculate_conflicts(best)}")
    return best, calculate_conflicts(best)

ga_nqueens()

# ── GA for Duty Scheduling ───────────────────────────────────
NUM_STAFF         = 5
NUM_SHIFTS        = 21
MAX_SHIFTS        = 7
REQ_PER_SHIFT     = 2
SCHED_POP_SIZE    = 10
SCHED_MUTATION    = 0.1
SCHED_GENERATIONS = 50

# Penalise under-staffed shifts and consecutive duty assignments
def sched_fitness(schedule):
    penalty = 0
    for shift in range(NUM_SHIFTS):
        assigned = sum(schedule[s][shift] for s in range(NUM_STAFF))
        if assigned < REQ_PER_SHIFT:
            penalty += (REQ_PER_SHIFT - assigned) * 10
    for s in range(NUM_STAFF):
        for shift in range(NUM_SHIFTS - 1):
            if schedule[s][shift] == 1 and schedule[s][shift + 1] == 1:
                penalty += 5
    return penalty

# Generate a random binary shift matrix (staff × shifts)
def random_schedule():
    schedule = [[0] * NUM_SHIFTS for _ in range(NUM_STAFF)]
    for s in range(NUM_STAFF):
        for shift in random.sample(range(NUM_SHIFTS),
                                   random.randint(3, MAX_SHIFTS)):
            schedule[s][shift] = 1
    return schedule

# Row-wise single-point crossover for schedules
def sched_crossover(p1, p2):
    pt = random.randint(0, NUM_SHIFTS - 1)
    return [p1[i][:pt] + p2[i][pt:] for i in range(NUM_STAFF)]

# Swap two shift assignments for a random staff member
def sched_mutate(schedule):
    s      = random.randint(0, NUM_STAFF - 1)
    s1, s2 = random.sample(range(NUM_SHIFTS), 2)
    schedule[s][s1], schedule[s][s2] = schedule[s][s2], schedule[s][s1]
    return schedule

population = [random_schedule() for _ in range(SCHED_POP_SIZE)]
for generation in range(SCHED_GENERATIONS):
    scores    = [sched_fitness(s) for s in population]
    best_fit  = min(scores)
    if generation % 10 == 0:
        print(f"Duty Scheduling Gen {generation+1}, Best Fitness: {best_fit}")
    sorted_pop = [x for _, x in sorted(zip(scores, population))]
    parents    = sorted_pop[:SCHED_POP_SIZE // 2]
    new_pop    = []
    while len(new_pop) < SCHED_POP_SIZE:
        p1, p2 = random.sample(parents, 2)
        child  = sched_crossover(p1, p2)
        if random.random() < SCHED_MUTATION:
            child = sched_mutate(child)
        new_pop.append(child)
    population = new_pop

final_scores  = [sched_fitness(s) for s in population]
best_schedule = population[final_scores.index(min(final_scores))]
print(f"Duty Scheduling Final Best Fitness: {min(final_scores)}")

# ============================================================
# LAB 06 - LAB TASKS
# ============================================================

# ── Task 1: 7-Queens Museum GA (camera placement) ────────────
CAM_N = 7  # 7x7 grid, 7 cameras

def cam_fitness(chromosome):
    """Count non-conflicting queen pairs. Max = 21."""
    conflicts = 0
    for i in range(CAM_N):
        for j in range(i + 1, CAM_N):
            if (chromosome[i] == chromosome[j] or
                    abs(chromosome[i] - chromosome[j]) == abs(i - j)):
                conflicts += 1
    return 21 - conflicts

# Generate a random permutation chromosome for camera placement
def cam_chromosome():
    return list(random.sample(range(CAM_N), CAM_N))  # permutation

# Tournament selection: pick best of k random individuals
def cam_select_tournament(population, k=3):
    contestants = random.sample(population, k)
    return max(contestants, key=cam_fitness)

def cam_ox_crossover(p1, p2):
    """Order Crossover (OX) for permutation chromosomes."""
    size   = len(p1)
    start, end = sorted(random.sample(range(size), 2))
    child  = [-1] * size
    child[start:end] = p1[start:end]
    ptr    = end
    for gene in p2[end:] + p2[:end]:
        if gene not in child:
            if ptr >= size:
                ptr = 0
            child[ptr] = gene
            ptr += 1
    return child

# Swap mutation: exchange two random positions
def cam_swap_mutate(chromosome):
    i, j = random.sample(range(CAM_N), 2)
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

# Full GA loop: evolve camera placements until no conflicts
def ga_museum_cameras():
    pop_size = 100
    max_gen  = 1000
    pop      = [cam_chromosome() for _ in range(pop_size)]

    for gen in range(max_gen):
        best = max(pop, key=cam_fitness)
        if cam_fitness(best) == 21:
            print(f"\nMuseum GA: Solution found at gen {gen}: {best}, Fitness: 21")
            return

        new_pop = []
        while len(new_pop) < pop_size:
            p1    = cam_select_tournament(pop)
            p2    = cam_select_tournament(pop)
            child = cam_ox_crossover(p1, p2)
            if random.random() < 0.1:
                child = cam_swap_mutate(child)
            new_pop.append(child)
        pop = new_pop

    best = max(pop, key=cam_fitness)
    print(f"\nMuseum GA: Best = {best}, Fitness: {cam_fitness(best)}")

ga_museum_cameras()

# ── Task 2: Selection Techniques (Roulette, Tournament, Rank) ─
chromosomes = ['C1', 'C2', 'C3', 'C4', 'C5']
fitnesses   = [12, 20, 15, 8, 25]

def roulette_wheel_selection(chroms, fits):
    """
    Roulette Wheel: each chromosome gets a slice of the wheel
    proportional to its fitness. Higher fitness = larger slice.
    """
    total  = sum(fits)
    probs  = [f / total for f in fits]
    r      = random.random()
    cumul  = 0
    for chrom, prob in zip(chroms, probs):
        cumul += prob
        if r <= cumul:
            return chrom
    return chroms[-1]

def tournament_selection(chroms, fits, k=3):
    """
    Tournament: pick k random chromosomes, return the fittest.
    Controls selection pressure via k.
    """
    indices     = random.sample(range(len(chroms)), k)
    best_idx    = max(indices, key=lambda i: fits[i])
    return chroms[best_idx]

def rank_selection(chroms, fits):
    """
    Rank Selection: rank chromosomes by fitness (worst=1, best=N),
    then apply roulette on ranks to reduce domination by very fit individuals.
    """
    ranked = sorted(range(len(fits)), key=lambda i: fits[i])
    ranks  = [0] * len(fits)
    for rank, idx in enumerate(ranked, 1):
        ranks[idx] = rank
    total  = sum(ranks)
    r      = random.random()
    cumul  = 0
    for chrom, rank in zip(chroms, ranks):
        cumul += rank / total
        if r <= cumul:
            return chrom
    return chroms[-1]

print("\n--- Task 2: Selection Techniques ---")
for _ in range(3):
    print("Roulette:", roulette_wheel_selection(chromosomes, fitnesses))
    print("Tournament:", tournament_selection(chromosomes, fitnesses))
    print("Rank:", rank_selection(chromosomes, fitnesses))
    print()

# ── Task 3: Crossover Techniques (One-Point, Two-Point, OX, Cyclic, PMX) ─
parent1 = [1, 3, 5, 0, 6, 4, 2]
parent2 = [2, 5, 1, 6, 0, 3, 4]

def one_point_crossover(p1, p2):
    """Split at one point and swap tails."""
    pt = random.randint(1, len(p1) - 1)
    return p1[:pt] + p2[pt:]

def two_point_crossover(p1, p2):
    """Split at two points and take middle from p1, ends from p2."""
    a, b = sorted(random.sample(range(1, len(p1)), 2))
    return p2[:a] + p1[a:b] + p2[b:]

def order_crossover(p1, p2):
    """
    OX Crossover (permutation-safe):
    Keep a segment from p1, fill rest from p2 in order.
    """
    size   = len(p1)
    a, b   = sorted(random.sample(range(size), 2))
    child  = [-1] * size
    child[a:b] = p1[a:b]
    ptr    = b
    for gene in p2[b:] + p2[:b]:
        if gene not in child:
            if ptr >= size:
                ptr = 0
            child[ptr] = gene
            ptr += 1
    return child

def cyclic_crossover(p1, p2):
    """
    Cyclic Crossover (CX): traces cycles between p1 and p2,
    alternating which parent contributes each cycle.
    Preserves the absolute position of each element.
    """
    size    = len(p1)
    child   = [-1] * size
    visited = [False] * size
    cycle   = 0
    for start in range(size):
        if not visited[start]:
            idx = start
            while not visited[idx]:
                visited[idx] = True
                child[idx]   = p1[idx] if cycle % 2 == 0 else p2[idx]
                idx          = p1.index(p2[idx])
            cycle += 1
    return child

def pmx_crossover(p1, p2):
    """
    Partially Mapped Crossover (PMX):
    Copy a segment from p1, fill remaining positions using
    a position-mapping derived from p2 to avoid duplicates.
    """
    size       = len(p1)
    a, b       = sorted(random.sample(range(size), 2))
    child      = [-1] * size
    child[a:b] = p1[a:b]
    for i in range(a, b):
        val = p2[i]
        if val not in child:
            pos = i
            while a <= pos < b:
                pos = p2.index(p1[pos])
            child[pos] = val
    for i in range(size):
        if child[i] == -1:
            child[i] = p2[i]
    return child

print("--- Task 3: Crossover Techniques ---")
print("One-Point  Crossover:", one_point_crossover(parent1, parent2))
print("Two-Point  Crossover:", two_point_crossover(parent1, parent2))
print("Order (OX) Crossover:", order_crossover(parent1, parent2))
print("Cyclic     Crossover:", cyclic_crossover(parent1, parent2))
print("PMX        Crossover:", pmx_crossover(parent1, parent2))

# ── Task 4: Mutation Techniques (Swap, Scramble, Inversion) ──
chromosome_base = [1, 3, 5, 0, 6, 4, 2]

def swap_mutation(chromo):
    """Randomly swap two positions."""
    chromo = chromo[:]
    i, j   = random.sample(range(len(chromo)), 2)
    chromo[i], chromo[j] = chromo[j], chromo[i]
    return chromo

def scramble_mutation(chromo):
    """Select a random subset and shuffle it."""
    chromo = chromo[:]
    a, b   = sorted(random.sample(range(len(chromo)), 2))
    subset = chromo[a:b]
    random.shuffle(subset)
    chromo[a:b] = subset
    return chromo

def inversion_mutation(chromo):
    """Select a segment and reverse it."""
    chromo = chromo[:]
    a, b   = sorted(random.sample(range(len(chromo)), 2))
    chromo[a:b] = reversed(chromo[a:b])
    return chromo

print("\n--- Task 4: Mutation Techniques ---")
print("Swap Mutation:      ", swap_mutation(chromosome_base))
print("Scramble Mutation:  ", scramble_mutation(chromosome_base))
print("Inversion Mutation: ", inversion_mutation(chromosome_base))

# ============================================================
# LAB 06 - Task 5: GA FITNESS FUNCTIONS
# How to define fitness for different problem domains
# (8-Puzzle, Maze, Chess Queens)
# ============================================================

# ── 5a. 8-Puzzle Fitness ─────────────────────────────────────
# Chromosome : permutation of [0..8], where 0 = blank tile
# Fitness    : number of non-blank tiles in their correct position (max = 8)
GOAL_8PUZZLE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def fitness_8puzzle(chromosome):
    """Count tiles (excluding blank) that are already in the goal position."""
    return sum(
        1 for i in range(9)
        if chromosome[i] == GOAL_8PUZZLE[i] and GOAL_8PUZZLE[i] != 0
    )

# Demo
sample_puzzle = [1, 2, 3, 4, 0, 6, 7, 5, 8]
print(f"\n--- 5a. 8-Puzzle Fitness ---")
print(f"Chromosome : {sample_puzzle}")
print(f"Goal       : {GOAL_8PUZZLE}")
print(f"Fitness    : {fitness_8puzzle(sample_puzzle)} / 8 tiles correct")

# ── 5b. Maze Fitness ─────────────────────────────────────────
# Chromosome : list of move indices  0=Up 1=Down 2=Left 3=Right
# Fitness    : negative Manhattan distance from final position to goal
#              (closer to goal = higher / less negative fitness)
MAZE_GRID  = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
]
MAZE_START = (0, 0)
MAZE_GOAL  = (4, 4)
MAZE_MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # U, D, L, R

def fitness_maze(chromosome):
    """
    Simulate the move sequence; return negative Manhattan distance
    from the agent's final position to the goal.
    Walls and out-of-bounds moves are simply ignored.
    """
    r, c   = MAZE_START
    rows   = len(MAZE_GRID)
    cols   = len(MAZE_GRID[0])
    for move in chromosome:
        dr, dc = MAZE_MOVES[move]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and MAZE_GRID[nr][nc] == 0:
            r, c = nr, nc
    return -(abs(r - MAZE_GOAL[0]) + abs(c - MAZE_GOAL[1]))

# Demo
sample_moves = [1, 1, 3, 1, 3, 1, 3, 3]   # a partial path attempt
print(f"\n--- 5b. Maze Fitness ---")
print(f"Moves   : {sample_moves}  (0=U 1=D 2=L 3=R)")
print(f"Fitness : {fitness_maze(sample_moves)}  (0 = goal reached)")

# Full GA loop: evolve move sequences to navigate the maze
def ga_maze(pop_size=100, chrom_len=20, max_gen=500, mutation_rate=0.1):
    population = [[random.randint(0, 3) for _ in range(chrom_len)]
                  for _ in range(pop_size)]
    for gen in range(max_gen):
        best = max(population, key=fitness_maze)
        if fitness_maze(best) == 0:
            print(f"Maze GA: solved at gen {gen}, moves: {best}")
            return best
        scored  = sorted(population, key=fitness_maze, reverse=True)
        parents = scored[:pop_size // 2]
        new_pop = []
        while len(new_pop) < pop_size:
            p1, p2 = random.sample(parents, 2)
            pt     = random.randint(0, chrom_len - 1)
            child  = p1[:pt] + p2[pt:]
            if random.random() < mutation_rate:
                child[random.randint(0, chrom_len - 1)] = random.randint(0, 3)
            new_pop.append(child)
        population = new_pop
    best = max(population, key=fitness_maze)
    print(f"Maze GA: best fitness {fitness_maze(best)}, moves: {best}")
    return best

ga_maze()

# ── 5c. Chess (Queens) Fitness ───────────────────────────────
# Same N-Queens concept framed as placing 8 chess queens on an 8x8 board.
# Chromosome : list of 8 column positions, one per row  (values 0–7)
# Fitness    : 28 - number of attacking pairs  (28 = max non-attacking pairs)
CHESS_N = 8

def fitness_chess_queens(chromosome):
    """
    Count attacking queen pairs; subtract from max (28) so that
    a perfect placement scores 28 and every conflict reduces the score.
    """
    attacks = 0
    for i in range(CHESS_N):
        for j in range(i + 1, CHESS_N):
            if (chromosome[i] == chromosome[j] or
                    abs(chromosome[i] - chromosome[j]) == abs(i - j)):
                attacks += 1
    return 28 - attacks

# Full GA loop: evolve queen placements until fitness = 28
def ga_chess_queens(pop_size=100, max_gen=1000, mutation_rate=0.1):
    population = [[random.randint(0, CHESS_N - 1) for _ in range(CHESS_N)]
                  for _ in range(pop_size)]
    for gen in range(max_gen):
        best = max(population, key=fitness_chess_queens)
        if fitness_chess_queens(best) == 28:
            print(f"Chess Queens GA: solved at gen {gen}: {best}")
            return best
        scored  = sorted(population, key=fitness_chess_queens, reverse=True)
        parents = scored[:pop_size // 2]
        new_pop = []
        while len(new_pop) < pop_size:
            p1, p2 = random.sample(parents, 2)
            pt     = random.randint(0, CHESS_N - 1)
            child  = p1[:pt] + p2[pt:]
            if random.random() < mutation_rate:
                child[random.randint(0, CHESS_N - 1)] = random.randint(0, CHESS_N - 1)
            new_pop.append(child)
        population = new_pop
    best = max(population, key=fitness_chess_queens)
    print(f"Chess Queens GA: best {best}, fitness {fitness_chess_queens(best)}")
    return best

print(f"\n--- 5c. Chess Queens Fitness ---")
print(f"Sample chromosome fitness: {fitness_chess_queens([0,4,7,5,2,6,1,3])}")
ga_chess_queens()

# ============================================================
# PAST PAPER Q3 - GENETIC ALGORITHM: INVESTMENT PORTFOLIO OPTIMISATION
# Goal : Maximise expected return while minimising risk (std-dev)
# Chromosome : list of N floats (asset allocations), sum = 1.0
#
# Modifications applied:
#   1. Elitism        – top 2 portfolios carried unchanged each gen
#   2. Uniform crossover – binary mask picks gene from p1 or p2
#   3. Dynamic mutation  – rate shrinks linearly: r*(1 - gen/max_gen)
#   4. Swap mutation     – swap two random allocation values
#   5. 40 % constraint   – heavy penalty if any asset > 0.40
# ============================================================

import random
import math

# ── Asset data ──────────────────────────────────────────────
ASSETS = ['Asset_A', 'Asset_B', 'Asset_C', 'Asset_D', 'Asset_E']

EXPECTED_RETURNS = [0.12, 0.18, 0.09, 0.15, 0.21]   # annual return per asset

# Covariance matrix (risk relationships between assets)
COV_MATRIX = [
    [0.005, 0.002, 0.001, 0.003, 0.002],
    [0.002, 0.010, 0.003, 0.004, 0.005],
    [0.001, 0.003, 0.004, 0.002, 0.001],
    [0.003, 0.004, 0.002, 0.008, 0.003],
    [0.002, 0.005, 0.001, 0.003, 0.009],
]

# GA hyper-parameters
PORT_POP_SIZE    = 50
PORT_MAX_GEN     = 100
PORT_INIT_RATE   = 0.15   # initial mutation rate (used for dynamic mutation)
PORT_ELITE_K     = 2      # [MOD 1] number of elite individuals to preserve
MAX_ALLOC        = 0.40   # [MOD 5] no single asset may exceed this fraction


# ── Helper: normalise chromosome so allocations sum to 1.0 ──
def normalise(chromosome):
    total = sum(chromosome)
    if total == 0:
        n = len(chromosome)
        return [1.0 / n] * n
    return [g / total for g in chromosome]


# ── Random chromosome ────────────────────────────────────────
def random_portfolio(n=len(ASSETS)):
    raw = [random.random() for _ in range(n)]
    return normalise(raw)


# ── Fitness function ─────────────────────────────────────────
def portfolio_fitness(chromosome):
    """
    Fitness = expected_return − risk_penalty − allocation_penalty
      • Higher expected return  → better
      • Higher portfolio variance → worse  (risk aversion)
      • [MOD 5] Any asset > 40 % → heavy penalty
    """
    n = len(chromosome)

    # Expected portfolio return
    exp_return = sum(chromosome[i] * EXPECTED_RETURNS[i] for i in range(n))

    # Portfolio variance  σ² = w^T · Σ · w
    variance = 0.0
    for i in range(n):
        for j in range(n):
            variance += chromosome[i] * chromosome[j] * COV_MATRIX[i][j]
    risk = math.sqrt(variance)   # standard deviation

    # [MOD 5] Penalty: heavy fine if any single asset exceeds 40 %
    alloc_penalty = 0.0
    for alloc in chromosome:
        if alloc > MAX_ALLOC:
            alloc_penalty += (alloc - MAX_ALLOC) * 10   # strong penalty

    return exp_return - risk - alloc_penalty


# ── [MOD 2] Uniform crossover ────────────────────────────────
def uniform_crossover(p1, p2):
    """
    For each gene position, randomly pick the value from p1 or p2
    using a binary mask.  Result is normalised to sum = 1.
    """
    mask  = [random.randint(0, 1) for _ in range(len(p1))]
    child = [p1[i] if mask[i] == 0 else p2[i] for i in range(len(p1))]
    return normalise(child)


# ── [MOD 4] Swap mutation ─────────────────────────────────────
def swap_mutation(chromosome):
    """
    Randomly choose two indices and swap their allocation values.
    Normalisation is not needed (sum is preserved by swapping).
    """
    chromo = chromosome[:]
    i, j   = random.sample(range(len(chromo)), 2)
    chromo[i], chromo[j] = chromo[j], chromo[i]
    return chromo


# ── Main GA ──────────────────────────────────────────────────
def genetic_algorithm_portfolio():
    # Initialise population
    population = [random_portfolio() for _ in range(PORT_POP_SIZE)]

    for generation in range(PORT_MAX_GEN):

        # [MOD 3] Dynamic mutation rate — decreases linearly each generation
        mutation_rate = PORT_INIT_RATE * (1 - generation / PORT_MAX_GEN)

        # Evaluate fitness for every individual
        scored = sorted(population,
                        key=lambda c: portfolio_fitness(c),
                        reverse=True)   # best (highest fitness) first

        # Progress print every 20 generations
        if generation % 20 == 0:
            best_fit = portfolio_fitness(scored[0])
            print(f"  Gen {generation:3d} | Best Fitness: {best_fit:.4f} "
                  f"| Mutation Rate: {mutation_rate:.4f}")

        # [MOD 1] Elitism — carry top PORT_ELITE_K unchanged into next gen
        new_population = scored[:PORT_ELITE_K]

        # Fill rest of population with children
        while len(new_population) < PORT_POP_SIZE:
            # Tournament selection (pick best of 3 random candidates)
            p1 = max(random.sample(population, 3), key=portfolio_fitness)
            p2 = max(random.sample(population, 3), key=portfolio_fitness)

            # [MOD 2] Uniform crossover
            child = uniform_crossover(p1, p2)

            # [MOD 4] Swap mutation (with dynamic rate from MOD 3)
            if random.random() < mutation_rate:
                child = swap_mutation(child)

            new_population.append(child)

        population = new_population

    # ── Final result ─────────────────────────────────────────
    best = max(population, key=portfolio_fitness)
    print("\n── Optimal Portfolio ──")
    for asset, alloc in zip(ASSETS, best):
        print(f"  {asset}: {alloc * 100:.2f} %")
    exp_ret  = sum(best[i] * EXPECTED_RETURNS[i] for i in range(len(ASSETS)))
    variance = sum(best[i] * best[j] * COV_MATRIX[i][j]
                   for i in range(len(ASSETS))
                   for j in range(len(ASSETS)))
    print(f"\n  Expected Return : {exp_ret * 100:.2f} %")
    print(f"  Portfolio Risk  : {math.sqrt(variance) * 100:.2f} %")
    print(f"  Fitness Score   : {portfolio_fitness(best):.4f}")
    return best


print("\n" + "═" * 50)
print("Genetic Algorithm — Investment Portfolio")
print("═" * 50)
genetic_algorithm_portfolio()

