# """
# Hello World
# """
# print("hello world")



# """
# 求和
# """
# def add(a,b):
#     return a+b
#
# a = input("请数据数字：")
# b = input("请输入数字：")
#
# print(add(float(a),float(b)))


# """
# 平方根，又叫二次方根，表示为〔√￣〕，如：数学语言为：√￣16=4。语言描述为：根号下16=4。
# 以下实例为通过用户输入一个数字，并计算这个数字的平方根：
# """
# def num_sqrt(a):
#     return  a ** 0.5
#
# print(num_sqrt(float(input("请输入数字："))))


# """
# 通过用户输入数字，并计算二次方程：
# """
# import cmath
# a = float(input("请输入a:"))
# b = float(input("请输入b:"))
# c = float(input("请输入c:"))
#
# delt = (b ** 2) - (4*a*c)
#
# r1 = (-b + (cmath.sqrt(delt))/(2*a))
# r2 = (-b - (cmath.sqrt(delt))/(2*a))
#
# print("this result is {0} and {1}".format(r1,r2))

# """
# 计算圆的面积
# """
# import math
# def calcArea(r):
#     return math.pi * (r*r)
#
# print("圆的面积为{0}".format(calcArea(float(input("请输入半径r:")))))


# """
# 随机数生成
# """
# import random
# print(random.randint(0,9))

# """
# 交换变量
# """
# a,b = 1,2
# print("a:{0};b:{1}".format(a,b))
# a,b=b,a
# print("a:{0};b:{1}".format(a,b))


# """
# if 语句
# """
# a = input("请输入:")
# print(isinstance(a,int))
# print(type(a))
# try:
#     a = float(a)
# except:
#     print("cant convert {0} to float".format(type(a)))
# print(isinstance(a,int))
# print(type(a))
# if(isinstance(a,float)):
#     if(a > 0):
#         print("this is a +")
#     elif(a < 0):
#         print("this is a -")
#     else:
#         print("this is 0")
# else:
#     print("It is not number")


# """
# 质数判断
# """
# a = int(input("please input a int number:"))
#
# if(a > 1):
#     for i in range(2,int(a/2)):
#         if(a%i == 0):
#             print(False)
#             break
#     else:
#         print(True)
# else:
#     print(True)


# """
# ASCII码与字符相互转换
# """
# c = input("please input a char:")
# a = int(input("please input a ASCII:"))
#
# print("{0}'s ASCII is {1}".format(c,ord(c)))
# print("{0}'s char is {1}".format(a,chr(a)))


# """
# 最大公约数算法
# """
# def maxhcf(a,b):
#     if(a<b):
#         i = a
#     else:
#         i = b
#         b = a
#     while (True):
#         if (b % i == 0):
#             return i
#         else:
#             i = i / 2
#
# a= int(input("please input a number:"))
# b= int(input("please input a number:"))
# print(maxhcf(a,b))


# str = "www.runoob.com"
# print(str.upper())
# print(str.lower())
# print(str.capitalize())
# print(str.title())


# 计算每个月天数
# import calendar
# monthRange = calendar.monthrange(2019,12)
# print(monthRange)

# import datetime
# def getYesterday():
#     today = datetime.date.today()
#     oneday = datetime.timedelta(days=1)
#     yesterday = today-oneday
#     return yesterday
# print(getYesterday())

# """
# 实现秒表功能
# """
# import time
# print("按下回车开始计时，按下Ctrl+c停止计时")
# while True:
#     try:
#         input()
#         starttime = time.time()
#         print("start")
#         while True:
#             print("计时：{0}秒".format(round(time.time()-starttime,0)))
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("结束")
#         endtime = time.time()
#         print("总共的时间为：{0}secs".format(round(endtime-starttime,2)))
#         break

# """
# 翻转集合
# """
# l = [10,11,12,13,14]
# print(l)
# result = reversed(l)
# l = list(result)
#
# print(l)

#
# """
# 判断元素是不是在列表中
# """
# testList = [10,12,13,14,15]
# if(testList.count(10) >0):
#     print(True)
# else:
#     print(False)
#
# """
# 清空列表
# """
# testList = [10,11,12,13,14,15]
# print(testList)
# print(testList.clear())
# print(testList)

# """
# 复制列表
# """
# one = ["a","b"]
# two = ["aa","bb"]
# list1=[one,two]
# # list2 = list1.copy()
# # list2 = list1[:]
# list2 = list(list1)
# t = list2[1]
# t.append("cc")
# print(list2)
# print(list1)

#
# """
# 统计数据之和
# """
# list1 = [10,11,12,13,14,15]
# count = 0
# for i in list1:
#     count += i
# print(count)

# """
# 删除字符串指定位置字符
# """
# str = "abcdefghij"
# print(str)
# print(str.replace(str[2],"",1))
# print(str)

# """
# 判断是否存在子串
# """
# str= "abcdefghijklmn"
# print(True if str.find("defg") > 1 else False)
# print(len(str))

# """
# 使用正则表达式获取字符串中的URL
# """
# import re
# def Find(string):
#     # findall() 查找匹配正则表达式的字符串
#     url = re.findall('https?://(?:[\w.]|(?:%[\da-fA-F]*))+', string)
#     return url
#
# string = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
# print("Urls: ", Find(string))

# """
# 执行字符串代码
# """
# str = "print(\"Hello World\")"
# exec(str)

# """
# 字符串翻转
# """
# str = "abcdefg"
# new_str = reversed(str)
# print("".join(new_str))


# """
# 截取自定字符串翻转
# """
# str = "abcdefg"
# print(""\
#       .join(reversed(str[:4]))\
#       +str[4:])

#
# """
# 对字典排序
# """
# dictTest = {"e":1,"g":2,"a":3,"h":4}
# print(sorted(dictTest.items()))
# print(sorted(dictTest.items(), key = lambda kv:(kv[1], kv[0])))


# """
# 对字典求和
# """
# dict = {'a': 100, 'b':200, 'c':300}
# count = 0
# for i in dict.keys():
#     count += dict[i]
# print(count)


# """
# 删除字典值
# """
# test_dict = {"Runoob" : 1, "Google" : 2, "Taobao" : 3, "Zhihu" : 4}
# print(test_dict)
# del test_dict["Runoob"]
# print(test_dict)
# test_dict.pop("Google")
# print(test_dict)


# """
# 合并字典
# """
# dict1 = {"a":1,"b":2}
# dict2 = {"aa":11,"bb":22,"a":12}
#
# dict1.update(dict2)
#
# print(dict1)

# dict1 = {"a":1,"b":2}
# dict2 = {"aa":11,"bb":22,"a":12}
# dict3 = {**dict1,**dict2}
# print(dict3)


# """
# 将字符串的时间转换为时间戳
# """
# import time
# a1 = "2019-5-10 23:40:00"
# timeArray = time.strptime(a1,"%Y-%m-%d %H:%M:%S")
# print(timeArray)
# timeStamp = int(time.mktime(timeArray))
# print(timeStamp)
#
# # 格式转换 - 转为 /
# a2 = "2019/5/10 23:40:00"
# # 先转换为时间数组,然后转换为其他格式
# timeArray = time.strptime(a2, "%Y/%m/%d %H:%M:%S")
# otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
# print(otherStyleTime)


# """
# 获取几天前的时间
# """
# import time
# import datetime
#
# threeDayAgo = datetime.datetime.now()-datetime.timedelta(days=3)
# print(threeDayAgo)
# timeStamp = time.mktime(threeDayAgo.timetuple())
# otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
# print(otherStyleTime)


# """
# 二分查找
# """
# def binaySearchExec(array,value,start,end):
#     if(start == end):
#         return -1
#     middle = int((start + end) / 2)
#     if array[middle] > value:
#         return binaySearchExec(array,value,start,middle)
#     elif array[middle] < value:
#         return binaySearchExec(array,value,middle,end)
#     else:
#         return middle
#
# def binarySearch(array,value):
#     return binaySearchExec(array,value,0,len(array)-1)
#
# arr = [1,2,3,4,5,6,7,8]
# print(binarySearch(arr,6))


# """
# 线性查找
# """
# def search(arr,value):
#     for i in range(0,len(arr)-1):
#         if arr[i] == value:
#             return i
# arr = ['a','b','c','d','e','f','g']
#
# print(search(arr,'f'))


# # """
# # 插入排序
# # """
# def insertSort(arr):
#     for i in range(len(arr),0,-1):
#         for j in range(i,0,-1):
#             if arr[i-1] < arr[j-1]:
#                 arr[i-1],arr[j-1] = arr[j-1],arr[i-1]
#
# a = [4,2,9,6,8,4,12,3,1]
# insertSort(a)
# print(a)

#
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)
# print(quicksort([3, 6, 8, 19, 1, 5]))  # [1，3, 5, 6, 8, 19]

# """
# 选择排序
# """
# def selectSort(arr):
#     for i in range(0,len(arr)):
#         min = i
#         for j in range(i+1,len(arr)):
#             if(arr[min] > arr[j]):
#                 min=j
#         arr[i],arr[min] = arr[min],arr[i]
#
# a = [4,2,9,6,8,4,12,3,1]
# selectSort(a)
# print(a)

#
# """
# 冒泡排序
# """
# def bubbleSort(arr):
#     for i in range(0,len(arr)):
#         for j in range(0,i):
#             if arr[i]<arr[j]:
#                 arr[i],arr[j] = arr[j],arr[i]
#
# a = [4,2,9,6,8,4,12,3,1]
# bubbleSort(a)
# print(a)




























