# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# for x in it:
#     print (x, end=" ")

# import sys
# list = [1,2,3,4]
# it = iter(list)
# while True:
#     try:
#         print(next(it),end="")
#     except StopIteration:
#         sys.exit()
#     print("-",end="")


import sys
def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if counter > n:
            return
        yield a
        a,b = b, a+b
        counter += 1
f = fibonacci(10)
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()
