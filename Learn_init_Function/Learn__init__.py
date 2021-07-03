class Mobile:

    def __init__(self, name, ph_num):
        self.name = name
        self.ph_num = ph_num

    def __str__(self):
        return "Gopi"


    def dial_num(self):
        print('dailing.......', self.ph_num)


    def send_SMS(self):
        print('sending.......', self.name, self.ph_num)


per1 = Mobile('Gopi', 54321)
print(per1)