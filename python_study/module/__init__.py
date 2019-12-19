from module import fibo
import sys

fibo.fib(100)
fiboResult = fibo.fib2(100)
print(fiboResult)


print("命令行參數如下")
for i in sys.argv:
    print(i)
print('\n\nPython路勁為：',sys.path,'\n')

tuple1 = (1,2,3,4)
print(tuple1)
arr = ["a","b","c","d"]
print(arr)
print(tuple(arr))
print(type(tuple1))
print(type(arr))
print(type(tuple(arr)))
dict1={"a":1,"b":2,"c":3}
print(dict1)
print(dict1["a"])

print("---------------------------------集合操作--------------------------")
parame = {123,53,"qwer","adfa","zcxv"}
print(parame)
for i in parame:
    print(i)
if(123 in parame):
    print("123 is OK")
else:
    print("123 is fail")
print("------------")
parame.remove("qwer")
print(parame)
parame.discard("qwer")
print(parame)

a,b = 0,2
while (b < 100):
    print(b,end=",")
    a,b=b,a+b

var = 1
while(var == 1):
    # num = int(input("請輸入一個數據："))
    num = 2
    result = 2
    if(num > 2):
        print("數據太大了")
    elif(num < 2):
        print("數據太小了")
    else:
        print("success")
        var = 0
print("----------------------------------for--------------")
a=["1","2","b","c","d","e"]
for i in range(len(a)):
    print(a[i])
else:print("is over")

for j in a:
    print(j)

for i in range(1,5):
    print(i)
for i in range(1,10,2):
    print(i)
print("---------------------pass語句-----------------")
for letter in "Runoob":
    if(letter == 'o'):
        pass
        print("執行pass塊")
    print("當前字母:",letter)
print("Good bye!")

print("-----------迭代器:iter() next()--------------------")
b=["q","w","e","for "]
it = iter(b)
print(next(it))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
myClass = MyNumbers()
myiter = iter(myClass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print("-----------------yield--------")
def fib(n):
    a,b,counter = 0,1,0
    while True:
        if(counter > n):
            return
        yield a         #返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
        a,b = b,a+b
        counter +=1

# f = fib(10)
# while True:
#     try:print(next(f),end=" ")
#     except StopIteration:
#         sys.exit()


print("--------------------")
for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(7),repr(x*x*x).rjust(4))

import pickle

data1 = {"a":[1,2.0,3,4+6j],
         "b":("String",u"Unicode String"),
         "c":None}
selfref_list = [1,2,3]
selfref_list.append(selfref_list)

output = open("data.pk1","wb")
pickle.dump(data1,output)
pickle.dump(selfref_list,output,-1)
output.close()

import pprint,pickle
pk1_file = open("data.pk1","rb")
data1 = pickle.load(pk1_file)
pprint.pprint(data1)
data2 = pickle.load(pk1_file)
pprint.pprint(data2)

pk1_file.close()


aa = [1,2,3,None,(),[]]
print(len(aa))

bb = 4
print(4 ** 0.5)








