class A:
    def process(self):
        print("Process A")
    def x(self):
        print("x")

class B(A):
    def process(self):
        print("Process B")
        # A.process(self)
        super().process()

class C(A):
    def process(self):
        print("Process C")
        super().process()

class D(B, C):
    def process(self):
        print("Process D")
        super().process()

d = D()
d.process()
d.x()
print(D.mro())