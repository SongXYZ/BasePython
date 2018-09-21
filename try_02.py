def input_password():
    pwd = input("Input password:")

    if len(pwd) >= 6:
        return pwd
    else:
        # 抛出异常
        print("主动抛出异常")
    # 创建异常对象
    ex = Exception("密码长度不够")
    # 主动抛出异常
    raise ex


try:
    print(input_password())
except Exception as result:
    print("%s" % result)
