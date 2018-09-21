try:
    num = int(input("Input integer:"))
    result = 8/num
except ZeroDivisionError:
    # 错误类型1
    print("Please > 0")
except ValueError:
    # 错误类型2
    print("Please a Input integer")
except Exception as result:
    # 打印未知错误
    print("Unknown error: %s" % result)
else:
    # 没有异常时执行的代码
    print(result)
finally:
    # 无论是否有异常,都会执行的代码
    print("finally")
