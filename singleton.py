# 单例模式 只生成对象的一个实例 比如：播放音乐


class MySingleton(object):

    flag = None
    init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.flag is None:
            cls.flag = super().__new__(cls)
        return cls.flag

    def __init__(self, name):
        if MySingleton.init_flag is True:
            print("初始化")
            MySingleton.init_flag = False
        self.name = name


player1 = MySingleton("tom")
print(player1.name)
player2 = MySingleton("ben")
print(player2.name)
print(player1)
print(player2)