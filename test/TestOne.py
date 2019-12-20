import random
import calendar
#
# #數字求和
# def sum(a,b):
#     return (a+b)
# print(sum(1,2))
#
# #平方根
# def sqrt(a):
#     return a**0.5
# print(sqrt(8))
#
# #隨機數
# def rundom():
#     return random.randint(1,9)
# print(rundom())
#
#
# a ,b = "10","20"
# a,b=b,a
# print(a)
# print(b)

# #判斷是否為一個數字
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except(TypeError,ValueError):
#         pass
#     return False
# print(is_number("asd"))

# def maxValue(s):
#     a = None
#     for i in range(len(s)):
#         if(i == 0):
#             a = s[0]
#         if(a < s[i]):
#             a = s[i]
#     return a
# a=[1,2,32,4,5,6]
# print(maxValue(a))

# def isZhiSu(num = 1023):
#     if num > 1:
#         for i in range(2,int(num/2 + 1)):
#             print(i)
#             if(num % i == 0):
#                 return False
#         else:return True
#     else:
#         return True
#
# print(isZhiSu(19))

# #階乘
# def factorial(num):
#     result = 1
#     while (num >= 1):
#         result *= num
#         num -= 1
#     return result
# print(factorial(10))

#乘法表
# def multTable():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print('{}x{}={}\t'.format(i,j,i*j),end=" ")
#         print()
# multTable()

# a = 10
# print("十進制：",a)
# print("二進制：",bin(a))
# print("八進制：",oct(a))
# print("十六進制：",hex(a))

# print(calendar.month(2019,1))

# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# print(fibo(20))
#
#
# def recur_fibo(n):
#     """遞歸函數 輸出斐波那契數列
#     """
#     if n <= 1:
#         return n
#     else:
#         return (recur_fibo(n-1)+recur_fibo(n-2))
# print(recur_fibo(20))

# with open("test.txt","rt") as in_file:
#     text = in_file.read()
# with open("test.txt","wt") as out_file:
#     out_file.write("這段文本會謝旭日")
# print(text)

# str = "runoob.com"
# print(str.isalnum())
# print(str.isalpha())
# print(str.capitalize())

# #計算每個月的天數
# monthRange = calendar.monthrange(2018,6)
# print(monthRange)

def gameOne():
    people= {}
    for i in range(1,31):
        people[i] = 1
    print(people)
    check = 0
    i = 1
    j = 0
    while i <= 31:
        if i == 31:
            i = 1
        elif j == 15:
            break
        else:
            if(people[i] == 0):
                i += 1
                continue
            else:
                check += 1
                if(check == 9):
                    people[i] = 0
                    check = 0
                    print("{}號碼下船了".format(i))
                    j += 1
                else:
                    i += 1
                    continue

gameOne()
























