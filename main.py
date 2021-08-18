# class Dog(object):
#     dogs = []
#
#     def __init__(self, name):
#         self.name = name
#         self.dogs.append(self)
#
#     def __str__(self):
#         return str(self.name)
#
#     @classmethod
#     def num_dogs(cls):
#         return len(cls.dogs)
#
#     @classmethod
#     def show_dogs(cls):
#         liste = [x for x in Dog.dogs]
#         return liste
#
#     @staticmethod
#     def bark(n):
#         for i in range(n):
#             print('bark')
#
#
# medor = Dog('medor')
# papa = Dog('papa')
# print(Dog.dogs)
# print(Dog.show_dogs())
# print(Dog.num_dogs())
#
# # liste = [x for x in range(10) if x %2 ==0]
# # print(liste)

liste = [1,1,1,12,2,23,3,3,2,1,3,4,5,3,24,45,67,54,34,76,8,5,54,65,86]
#
# print([x**2 for x in liste])
#
# def func(x):
#     return x*x
#
# print([func(x) for x in liste])
# print(list(map(func, liste)))

# def isOdd(x):
#     return x%2 != 0
#
# print(list(filter(isOdd, liste)))
#
# print(list(filter(lambda x:x%2==0, liste)))

## SET ##
s = {x for x in liste}
print(s)