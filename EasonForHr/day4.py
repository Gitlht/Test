class car:
    wheel_sum = 4

    @staticmethod
    def space(l, w, h):
        v = l * w * h
        return v

    def __init__(self, brand):
        self.brand = brand


car1 = car("宝马")
print(car1.brand, car1.space(2, 3, 5), car1.wheel_sum)
