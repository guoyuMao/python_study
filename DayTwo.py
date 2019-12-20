# -*- coding:utf-8 -*-
import sys
import HelloWorld
print(sys.argv)

# str = "  welcome to China  "
# print(len(str))
# str = str.strip()
# print(len(str))
# print(str)
# for i in range(len(str)):
#     print('''%s ''' %(str[i]))
# print(str[1:])
# print(str[-3:])
# print(str[0:6])
# print(str[0:8:2])

# a = [1,2,3,4,5,6]
# print(a)
# print(a[0:4])
#
# a = (1,2,{'k1':'s1'})
# a[2]['k1'] = 3
# print(a)

# all = 95
# pager = 10
# result = all.__divmod__(10)
# print(result)
# print(all.__rdivmod__(10))

# age = 18
# print(age.__le__(19))
# print(age.__ge__(18))
#
# print(age.__gt__(19))
# print(age.__eq__(18))

# age = 10
# str = "10"
#
# print(type(age))
# print(type(HelloWorld.file_obj))
# print(dir(age))
# print(dir(str))
# print(dir(HelloWorld.file_obj))

# str = "qwertyuip"
# print(str.capitalize())
# print(str.center(20))
# print(str.title())


# s = ['h','e','l','l','o']
# print(s)
# result = "".join(s)
# print(result)
# print("-".join(s))

# name = "YouneedPython"
# result = name.partition("need")
# print(result)


# name = '''
# aa
# bb
# cc
# '''
# print(type(name))
# result = name.splitlines()
# print(type(result))
# print(result)

# dic = dict(a1='b1',a2='b2')
# new_dict = dic.fromkeys(['a1','a2','a3'],'b1')
# print(new_dict)

# dic = dict(a1='b1',a2='b2')
# print(dic.get("a1"),dic['a1'])
# print(dic.get('a3',"aaa"))

dic = {}
all_list = [11,22,33,44,55,66,77,88,99]
for i in all_list:
    if i > 66:
        if "k1" in dic.keys():
            dic['k1'].append(i)
        else:
            dic['k1'] = [i]
    else:
        if "k2" in dic.keys():
            dic['k2'].append(i)
        else:
            dic['k2'] = [i]
print(dic['k1'])
print(dic['k2'])
print(dic)
