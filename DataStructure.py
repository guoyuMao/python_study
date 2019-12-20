# vec = [2,4,6]
# test = [3*x for x in vec]
# print(test)
#
# test = [[x,x**2] for x in vec]
# print(test)
#
#
# freshfruit=[' banana',' loganberry ',' passion fruit  ']
# test = [weapon.strip() for weapon in freshfruit]
# print(test)
#
# test = [3*x for x in vec if x > 3]
# print(test)
#
# test = [3*x for x in vec if x <= 2]
# print(test)


# vec1 = [2,4,6]
# vec2 = [4,3,-9,10]
# print([x*y for x in vec1 for y in vec2])
# print([x+y for x in vec1 for y in vec2])
# print([vec1[i] * vec2[i] for i in range(len(vec1))])

# matrix = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
#
# test = [[row[i] for row in matrix] for i in range(4)]
# print(test)
#
# print(len(matrix))
#
# t = [[row[i] for i in range(len(row))]for row in matrix]
# print(t)
#
#
# transpose = []
# for i in range(4):
#     transpose.append([row[i] for row in matrix])
# print(transpose)
#
# transposed =[]
# for i in range(4):
#     transpose_row = []
#     for row in matrix:
#         transpose_row.append(row[i])
#     transposed.append(transpose_row)
# print(transposed)

# a = [-1,1,66.25,333,333,1234.5]
# del a[0]
# print(a)
#
# del a[2:4]
# print(a)

# del a[:]
# print(a)


# t = 12345,54321,"hello!"
# print(t[0])
# print(t)
#
# u = t,(1,2,3,4)
# print(u)


# basket = {'apple','orange','apple','pear','orange','banana'}
# print(basket)
# print('orange' in basket)


# a = set('aasdgdsg')
# b = set("adsfds")
# print(a)
# print(b)

# c = {"afds","dafds","dafds"}
# print(c)
# for a in c:
#     print(a)



# tel = {"jajfds":1234,"fadsf":809}
# print(tel)
# print(tel.get("jajfds"))
# print(tel.get("fadsf"))
# print(tel.values())

# list = [("daf",1234),("dad",89),("liu",80)]
# print(list)
# for a in list:
#     print(a)

# dic = dict(list)
# print(dic)
# dictTest = {x:x**2 for x in (2,4,6)}
# print(dictTest)
# print(type(dictTest))
# print(type({x:x**2 for x in (2,4,6)}))
# print({x:x**2 for x in (2,4,6)})


# knights = {"adfds":"adfd","daf":"ioaid","int":134}
# print(knights)

# print(type(["tic","tac","toe"]))
# for i,v in enumerate(["tic","tac","toe"]):
#     print(i,v)
#
# questions = ["name","quest","favorite color","test"]
# answers = ['lancelot',"the holy grail","blue"]
# print(type(zip (questions,answers)))
# print(zip(questions,answers))
# for q,a in zip (questions,answers):
#     print("What is you {0}? It is {1}".format(q,a))

# import time
# print("current time ticks is {0}".format(time.time()))
# localtime = time.localtime(time.time())
# print("current localtime is {0}".format(localtime))
# print(type(localtime))
# print(localtime.tm_year)
#
# import calendar
# print(calendar.month(2019,9))
# print(id(calendar))
# import sys
# print(sys.path)
#
# money = 1
# def add_money():
#     global money
#     print(money)
#     money =  money  + 1
# add_money()

# print(globals())
# print(locals())
#
# str = input("请输入")
# print(str)

# class FooParent(object):
#     def __init__(self):
#         self.parent = 'I\'m the parent.'
#         print('Parent')
#
#     def bar(self, message):
#         print("%s from Parent" % message)
#
#
# class FooChild(FooParent):
#     def __init__(self):
#         # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
#         super(FooChild, self).__init__()
#         print('Child')
#
#     def bar(self, message):
#         super(FooChild, self).bar(message)
#         print('Child bar fuction')
#         print(self.parent)
#
# class test(FooChild):
#     def __init__(self):
#         super(test,self).__init__()
#         print("test init")
#
#     def bar(self, message):
#         print("test basr")
#
#
#
# if __name__ == '__main__':
#     fooChild = FooChild()
#     fooChild.bar('HelloWorld')
#
#     print("----------------------")
#     test = test()
#     test.bar("aaaaa")
# class Test_a:
#     def __init__(self,p):
#         a = p
#     def get(self):
#         return self.a
#
#
# dict = [Test_a(1),Test_a(2),Test_a(3)]
# for i in iter(dict,Test_a.get()):
#     print(i)

#############################面向对象###################################

# class Employee:
#     "所有员工的基类"
#     empCount = 0
#
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print("Total Employee {0}".format(Employee.empCount))
#
#     def displayEmploys(self):
#         print("Name :{0}, salary:{1}".format(self.name,self.salary))
#
# emp1 = Employee("Zara",2000)
# emp2 = Employee("Manni",5000)
#
# emp1.displayEmploys()
# emp2.displayEmploys()
# print("Total Employee {0}".format(Employee.empCount))
#
# print("Employee.__doc__:{0}".format(Employee.__doc__))
# print("Employee.__name__:{0}".format(Employee.__name__))
# print("Employee.__module__:{0}".format(Employee.__module__))
# print("Employee._bases__:{0}".format(Employee.__bases__))
# print("Employee.__dict__:{0}".format(Employee.__dict__))

################################垃圾回收#############################
# class Point:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         class_name = self.__class__.__name__
#         print(class_name)
#
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
#
# print(id(pt1),id(pt2),id(pt3))
# del pt1
# del pt2
# del pt3



######运算符重载#############
# class Vector:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return "Vector ({0},{1})".format(self.a,self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a,self.b+other.b)
#
# v1 = Vector(2,10)
# v2 = Vector(5,-1)
# print(v1 + v2)

#########类属性与方法########
# class JustCount:
#     __secretCount = 0       # 私有变量
#     publicCount = 0         # 公开变量
#
#     def __secretMethod(self):
#         """私有方法"""
#         print("this is secret method!")
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#         self.__secretMethod()
#
#
# counter = JustCount()
# counter.count()
# counter.count()
# print(counter.publicCount)





