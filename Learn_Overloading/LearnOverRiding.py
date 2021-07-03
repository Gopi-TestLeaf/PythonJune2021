class A:

    def get_data(self):
        print("hello")

    def set_data(self):
        print("update")



class B(A):

    def get_data(self):
        print('hi')

x = B()
x.get_data()
