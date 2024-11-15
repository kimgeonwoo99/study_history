from Addr1 import Addr1
from Addr2 import Addr2

class CompanyAddr(Addr1,Addr2):
    def __init__(self, name, phone, email, address, group, birthday, company, department, position):
        super().__init__(name,phone,email,address,group,birthday,position)
        self.__company = company
        self.__department = department

    def get_company(self):
        return self.__company
    def set_company(self,value):
        self.__company = value

    def get_department(self):
        return self.__department
    def set_department(self, value):
        self.__department = value

    def print_info(self):
        super().print_info()
        print(f"회사이름 : {self.get_company()}")
        print(f"부서이름 : {self.get_department()}")
        print(f"직급 : {self.get_position()}")

    def showData(self,addr):
        super().showData(addr)


