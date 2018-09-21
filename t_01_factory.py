# 工厂模式 用来实例化对象


class CarFactory(object):

    @staticmethod
    def creat_car(brand):
        if brand == "Benz":
            return Benz()
        elif brand == "BYD":
            return BYD()
        elif brand == "BMW":
            return BMW()
        else:
            return "wufachuangjian"


class Benz:
    pass


class BYD:
    pass


class BMW:
    pass


factory = CarFactory()
c1 = factory.creat_car("Benz")
c2 = factory.creat_car("BYD")

print(c1)
print(c2)
