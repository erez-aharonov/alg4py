import alkh
alkh.analyze()


class A:
    k = 8

    def __init__(self):
        b = 8 + self.k
        pass

    @staticmethod
    def run(
            n):
        a = 5
        b = a + 7 + 5.0
        ll = a + 6.4
        c = a + b + 3
        d = b + c
        k = d * 2


class B:
    def __init__(self):
        b = 8
        pass

    def run(self):
        a = 5
        b = a + 7 + 5.0
        ll = a + 6.4
        c = a + b + 3
        d = b + c
