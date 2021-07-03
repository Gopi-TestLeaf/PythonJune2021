class A:

    def a(self):
        print("I'm from class A")


class B(A):

    def b(self):
        print("I'm from class B")


class C(B):

    def c(self):
        print("I'm from class C")


cc = C()
cc.c()
cc.b()
cc.a()
