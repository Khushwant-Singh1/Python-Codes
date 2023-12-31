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


# class Employee:
#     salary = 1000
#     increment = 1.5
#
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary*self.increment
#
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, sai):
#         self.increment = sai/self.salary
#
# e = Employee()
# print(e.salaryAfterIncrement)
# e.salaryAfterIncrement = 2000
# print(e.salaryAfterIncrement)
# print(e.increment)



# # (a+bi)(c+di) = (ac-bd) + (ad+bc)i
# class Complex:
#     def __init__(self, r, i):
#         self.real = r
#         self.imaginary = i
#
#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imaginary + other.imaginary)
#
#     def __mul__(self, other):
#         mulReal = (self.real*other.real - self.imaginary*other.imaginary)
#         mulImg = self.real*other.imaginary + self.imaginary*other.real
#         return Complex(mulReal, mulImg)
#
#     def __str__(self):
#         return f"{self.real} + {self.imaginary}i"
#
# c1 = Complex(1,4)
# c2 = Complex(8,5)
# print(c1+c2)
# print(c1*c2)

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str += f"{i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, other):
        newList = []
        for i in range (len(self.vec)):
            newList.append(self.vec[i] + other.vec[i])
        return Vector(newList)

    def __mul__(self, other):
        sum = 0
        for i in range(len(self.vec)):
            x = self.vec[i]*other.vec[i]
            sum += x
        return sum

    def __len__(self):
        return len(self.vec)

v1 = Vector([1, 4])
v2 = Vector([1, 6])
print(v1 + v2)
print(len(v1))
print(len(v2))
