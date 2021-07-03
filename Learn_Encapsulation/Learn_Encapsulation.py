# Ecanpsulation:
# Data Hiding
# Implementation Hiding


class TestLeaf:

    tl_ph_num = 1234567821
    goff_num = 5432154321
    _gpersonal = 123456789

    def data_science(self):
        print("DS")

    def selenium(self):
        print("Web")

    def _arrangeInt(self):
        print('Related to interview session')

    def get_data(self):
        return TestLeaf._gpersonal

    def set_data(self, newNum):
        TestLeaf._gpersonal = newNum

    def accessPrivateMethod(self):
        TestLeaf._arrangeInt(self)


per1 = TestLeaf()

gnum = per1.get_data()
print(gnum)

per1.set_data(987654321)

gnum = per1.get_data()
print(gnum)

per1.accessPrivateMethod()


