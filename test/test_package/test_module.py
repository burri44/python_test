'''
Created on Dec 26, 2019

@author: nicolaburri
'''
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'Gcompany.com'
        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)
        

emp_1 = Employee('Corey', 'Schaefer', 50000)
emp_2 = Employee('Cedi', 'Cedigang', 10000)



print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)