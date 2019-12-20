# s1 = set([11,22,33])
# s2 = set({22,44})
#
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))

# import collections
# f = collections.Counter("abcdefghijklmn")
# print(f)


# import  collections
# mytupleclass = collections.namedtuple('mytupleclass',['x','y','z'])
# print(mytupleclass)
# obj = mytupleclass(11,22,33)
# print(obj)
#
# print(obj.x)
# print(obj.y)
# print(obj.z)

# import copy
# dic = {"cpu":[80,70],"mem":[80],"disk":[80]}
# print('before',dic)
# new_dic = copy.copy(dic)    #浅拷贝
# new_dic["cpu"][0] = 50
# print(dic)
# print(new_dic)
# print("-------------")
# new_dic = copy.deepcopy(dic) #森拷贝
# new_dic['cpu'][1]=10
# print(dic)
# print(new_dic)

# import smtplib
# from email.mime.text import MIMEText
# from email.utils import formataddr
#
# def mail():
#     ret = 'success'
#     try:
#         msg = MIMEText("mail context","plain","utf-8")
#         msg['From'] = formataddr(["111","1126208518@qq.com"])
#         msg['To'] = formataddr(["222","910603212@qq.com"])
#         msg['Subject'] = "topic"
#
#         server = smtplib.SMTP("smtp.qq.com",25)
#         server.login("1126208518@qq.com","love1314520240")
#         server.sendmail("1126208518@qq.com",['910603212@qq.com,'],msg.as_string())
#         server.quit()
#     except Exception:
#         ret = "fail"
#     return ret
# ret = mail()
# print(ret)


