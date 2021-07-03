class GA:

    def ga(self):
        print("I'm from GA")

    def com(self):
        print("I'm from GA")


class GB:

    def gb(self):
        print("I'm from GB")

    def com(self):
        print("I'm from GB")


class A(GA, GB):

    def a(self):
        print("I'm from class A")

    def za(self):
        print("I'm from class A")

    def com(self):
        print("I'm from A")


class B:

    def b(self):
        print("I'm from class B")

    def z(self):
        print("I'm from class B")

    def com(self):
        print("I'm from B")


class C(A, B):

    def c(self):
        print("I'm from class C")

cc = C()
cc.com()
print(C.__mro__)     #(Method Resolution Order)


