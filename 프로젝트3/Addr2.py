from ShowData import ShowData
from Addr1 import Addr1

class Addr2(ShowData):
    def __init__(self,name,phone,email,address,group,birthday,position):
        self.addr = Addr1(name,phone,email,address,group,birthday,position)

    def showData(self,addr):
        print(f"이름 : {addr.get_name()}")
        print(f"전화번호 : {addr.get_phone()}")