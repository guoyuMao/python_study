try:
    # with open("testOne.txt", "r", encoding="utf-8") as testOne:
    #     print(testOne.read())
    #     print("*"*30)
    #     print(testOne.readline())
    #     for line in testOne:
    #         print(line)

    # with open("testOne.txt","w+",encoding="utf-8") as testOne:
    #     print(testOne.writable())
    #     print(testOne.write("你好\n"))
    #     print(testOne.writelines({"你好","测试"}))
    #     print(testOne.writelines(["哈哈哈","嘿嘿"]))
    #     print(testOne.read())

    with open("picture/sch_rules.png","rb") as pic:
        data = pic.read()
        print(type(pic))
        # print(pic.read())
    with open("picture/1.png","wb") as one:
        one.write(pic.read())

except FileNotFoundError:
    print("not found file")
except LookupError:
    print("指定了未知编码")
except UnicodeDecodeError:
    print("读取文件时解码错误")
