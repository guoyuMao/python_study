# def area(width,heigh):
#     return heigh * width
#
# print("please input width:")
# w = int(input())
# print("please input height:")
# h = int(input())
# print("this area is : %d" %area(w,h))


'''不可变对象与可变对象'''
#不可变对象
# def changeInt(a):
#     a = 10
# b = 2
# changeInt(b)
# print(b)
# #可变对象
# def changeme(list):
#     list.append(['q','w',3,4])
#     print("函数内部值：",list)
#     # return
# mylist = [10,2,53]
# changeme(mylist)
# print("函数外不值：",mylist)

#
# def printinfo(arg,*vartuple):
#     print("输出:")
#     print(arg)
#     for var in vartuple:
#         print(var)
#     return
#
# printinfo(10)
# printinfo(70,4,2,23,12)


# sum = lambda arg1,arg2,arg3:arg1 + arg2
# print(sum(2,34,5))
# print(sum(52,12,43))

# total = 0
# def sum(arg1,arg2):
#     total = arg1+ arg2
#     print("函数内饰局部变量：",total)
#     return total
#
# sum(10,20)
# print("函数外是全局变量：",total)

# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
# num = 1
# def fun1():
#     global num  #指定num是全部作用于的变量
#     print(num)
#     num  = 123
#     print(num)
# fun1()
# print(num)

# def outer():
#     num = 10
#     def inner():
#         nonlocal num
#         num = 100
#         print(num)
#     print(num)
#     inner()
#     print(num)
# outer()


