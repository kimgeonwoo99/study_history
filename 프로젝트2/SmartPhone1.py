from CompanyAddr import CompanyAddr
from CustomerAddr import CustomerAddr
from SmartPhone_teacher import SmartPhone

class SmartPhone1(SmartPhone):
    def __init__(self):
        self.contacts = []

    def input_addr_data_Com(self):
        name = input("이름 : ")
        phone = input("전화번호 : ")
        email = input("이메일 : ")
        address = input("주소 : ")
        birthday = input("생일 : ")
        group = input("그룹 (회사 / 거래처) : ")
        company = input("회사 이름 : ")
        department = input("부서 이름 : ")
        position = input("직급 : ")
        return CompanyAddr(name, phone, email, address, group, birthday, company, department, position)
    
    def input_addr_data_Cus(self):
        name = input("이름 : ")
        phone = input("전화번호 : ")
        email = input("이메일 : ")
        address = input("주소 : ")
        birthday = input("생일 : ")
        group = input("그룹 (회사 / 거래처) : ")
        company = input("거래처 이름 : ")
        item = input("품목 이름 : ")
        position = input("직급 : ")
        return CustomerAddr(name, phone, email, address, group, birthday, company, item, position)
    
    def add_addr(self, addr):
        super().add_addr(addr)

    
    def print_all_addr(self):
        super().print_all_addr()

    
    def search_addr(self, name):
        super().search_addr(name)

    def delete_addr(self, name):
        super().delete_addr(name)
    
    def edit_addr(self, name, new_addr):
        super().edit_addr(name, new_addr)         
