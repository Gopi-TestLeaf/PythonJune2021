class Test_Data:

    def __init__(self, **kwargs):
        self.fName = kwargs['fName']
        self.lName = kwargs['lName']
        self.eMail = kwargs['eMail']
        self.pwd = kwargs['pwd']


# obj = Test_Data(fName="Gopinath", lName="Jayakumar", eMail="g@gmail.com", pwd=54321)
# print(obj.fName)