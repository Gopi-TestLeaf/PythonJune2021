class Hospital:

    def __init__(self):
       pass

    def doctor(self):
        print("doc Name")        # instance Method


    def adm(self):
        print('Admin')

    @classmethod
    def police_info(cls):
        print('Police equ')                 # Class Method

    @staticmethod
    def yogo_details():
        print("some of info")               # static Method

d1 = Hospital()
d1.adm()
d1.doctor()

d1.police_info()
Hospital.police_info()


Hospital.yogo_details()