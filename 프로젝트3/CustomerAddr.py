from Addr1 import Addr1
from Addr2 import Addr2

class CustomerAddr(Addr1, Addr2):
    def __init__(self, name, phone, email, address, group, birthday, company, item, position):
        super().__init__(name,phone,email,address,group,birthday,position)
        self.__company = company
        self.__item = item

    def get_company(self):
        return self.__company
    def set_company(self,value):
        self.__company = value

    def get_item(self):
        return self.__item
    def set_item(self, value):
        self.__item = value

    def print_info(self):
        super().print_info()
        print(f"거래처 이름 : {self.get_company()}")
        print(f"품목 이름 : {self.get_item()}")
        print(f"직급 : {self.get_position()}")

    def showData(self,addr):
        super().showData(addr)
