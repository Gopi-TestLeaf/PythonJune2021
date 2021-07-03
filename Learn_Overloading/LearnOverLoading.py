class OverLoadingClass:

    def __init__(self, *args):
        print(len(args))


    def add(self, a):
        return a


    def add(self, b):
        return b


x = OverLoadingClass(1, 2, 3, 4, 5)
y = OverLoadingClass('a', 'b', 'c')

