class employee:
    def __init__(self,age):
        self.age=age
    def superage(self):
        return(self.age+10)
age=int(input("Enter your age"))
emp=employee(age)

print(emp.age)
print(emp.superage())
print(emp.age)
a=[1,2,3,4]
print(str(a))
print(a)
