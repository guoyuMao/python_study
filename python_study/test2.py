# import sys
# print("=====================python import mode============")
# print("the cmd param is :")
# for i in sys.argv:
#     print(i)
# print("\n pthon path is :",sys.path)

#
# from sys import argv,path
# print(argv)
# print(path)

'''
data type:
    Number
    String
    Tuple
    Sets
    List
    Dictionary
'''

# #Number
# a,b,c,d = 20,5.5,True,4+3j
# print(type(a),type(b),type(c),type(d))
# print(isinstance(a,int))
# print(isinstance(b,int))

# #String
# str ="welcome to china"
# print(str)
# print(str[0:3])
# print(str[-3:-1])

#与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。


#List  列表是写在方括号([])之间、用逗号分隔开的元素列表。
# 与字符串不一样的是，列表中的元素是可以改变的
# list = ['abcd','786',2.34,'runoob',703]
# tinylist = [123,'runoob']
# print(list)
# print(list[0])
# print(list[0:3])
# print(list[2:])
# print(tinylist * 2)
# print(list + tinylist)

# a = [1,2,3,4,5,6]
# a[0] = 9
# print(a)
# a[2:5] = []
# print(a)

#Tuple
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开
# tuple = ('abcd',786,2.23,'runoob',70.2)
# tinytuple = (123,'runoob')
# print(tuple)
# print(tuple[0])
# print(tuple[1:3])
# print(tuple[2:])
# print(tinytuple * 2)
# print(tuple + tinytuple)
#
# tup1 = ()
# tup2 = (12,)
# print(tup1)
# print(tup2)
# print(len(tup2))

#Set
# 集合（set）是一个无序不重复元素的序列。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# set1 = {12,34,12,56}
# print(len(set1))
# print(set1)

# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# print(student)
# #成员测试
# if("Rose" in student):
#     print("Rose is in the Set")
# else:
#     print("Rose is not in the Set")
#
# a = set("abcadfa")
# b = set("asdfad")
# print(a,b)
#
# print(a -b)
# print(a | b)
# print(a & b)
# print(a ^ b)


#Dictionary
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。
# dict = {}
# dict['one'] = "1"
# dict[2] = "Two"
# tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
#
# print(dict['one'])
# print(dict[2])
# print(tinydict)
# print(tinydict.keys())
# print(dict.values())

#构造函数 dict() 可以直接从键值对序列中构建字典如下：
# key_map = dict([("Runoob",1),("Google",2),("taobao",3)])
# print(key_map)

key_map1 = {x:x**2 for x in (2,4,6,8)}
print(key_map1)

# print(dict(Runoob = 1,Google = 2,Taobaoo = 3))
