# class C2dVec:
#      def __init__(self, i, j):
#          self.icap = i
#          self.jcap = j
#
#      def __str__(self):
#          return f"{self.icap}i + {self.jcap}j"
#
# class C3dVec(C2dVec):
#
#     def __init__(self, i, j, k):
#         self.kcap = k
#         super().__init__(i,j)
#
#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
#
#
# v2d = C2dVec(1,3)
# v3d = C3dVec(1,9,7)
# print(v2d)
# print(v3d)

# class Animals:
#     animalType = "Mammal"
# 
# class Pets:
#     color = "White"
# 
# class Dog:
#     @staticmethod
#     def bark():
#         print("Bow bow!")
# 
# d = Dog()
# d.bark() 


class Employee:
    salary = 1000
    increment = 1.5
    
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 2000
print(e.salaryAfterIncrement)
    