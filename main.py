from logging import lastResort
from traceback import print_stack

print("UNIT testing")
def add (a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        # raise შექმნის ერორს ხელოვნურად, მაგ: თუკი type ან zerodivisionerror, გარდაქმნის იმ ერორად რომლსაც გავუწერთ და გამოიყანს იმას რასაც ჩვენ გავუწერთ მნიშვნელობაში
        raise ValueError("division by zero")
    return a / b

print(div(2, 0))


def is_even(a):
    return a % 2 == 0

# class / object##############################################################################################################################

# number = float(input("Enter a number: "))

class Student:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    def get_email(self, domain):
        return f"{self.first_name}.{self.last_name}@{domain}"

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def discount(self, num):
        return self.pay * num


st1 = Student("malkhaz", "okriashvili", 10000)

print(st1.discount(0.5))
print(st1.get_full_name)








