# 打开文件
file = open("./hello")

# 读取文件
# text = file.read()
while True:
    text = file.readline()

    if not text:
        break

    print(text)
    print(len(text))

# 关闭文件
file.close()
