def say_hello():
    print("say hello")


# 测试代码
def main():
    print(__name__)
    say_hello()


# 如果直接执行模块, 输出__main__
# 执行测试代码
if __name__ == "__main__":
    main()
