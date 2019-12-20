# name = input("please input you name:").strip()
# age = int(input("please input you age:"))
# job = input("please input you job").strip()
# print("you information is %s:\nName:%s\nAge:%d\nJob:%s" %(name,name,age,job))
#
# mesg = """
#     information is %s:
#     name:%s
#     age:%d
#     job:%s"""
# print(mesg %(name,name,age,job))


# arr = [1,2,3,4,5,6,7,8]
# print(arr[1:3])
# print(arr)
# print(arr[-5:])
#
# print(arr[-4:-1:1])


# for j in range(5):
#     for i in range(10):
#         if i < 5:
#             continue
#         if j > 3:
#             break
#         print(i)
#     print("\n")

file_obj = open("E:\python_workspace\helloWorld\\file\\testTwo.txt","w")
file_obj.write("this is 1\n")
file_obj.write("this is 2\n")
file_obj.close()


