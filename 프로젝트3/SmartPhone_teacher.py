# SmartPhone 클래스 만들기 

from Address_teacher import Addr

class SmartPhone:
    def __init__(self):
        self.contacts = [] # 10개의 연락처를 저장할 리스트 생성

    def input_addr_data(self):
        # 사용자로부터 정보를 입력 받음
        name = input("이름을 입력하세요 : ")
        phone = input("전화번호를 입력하세요 : ")
        email = input("이메일을 입력하세요 : ")
        address = input("주소를 입력하세요 : ")
        group = input("그룹을 입력하세요 (가족 / 친구) : ")
        return Addr(name, phone, email, address, group)
    
    def add_addr(self, addr):
        if len(self.contacts) < 10:
            self.contacts.append(addr)
            print("데이터가 저장되었습니다.")
        else :
            print("연락처 저장 공간이 가득 찼습니다.")

    def print_all_addr(self):
        if not self.contacts:
            print("저장된 연락처가 없습니다.")
        else:
            for i, addr in enumerate(self.contacts):
                print(f'\n[{i+1}]')
                addr.print_info()
                
    def search_addr(self, name):
        for addr in self.contacts:
            if addr.get_name() == name:
                addr.print_info()
                return
        print(f"{name}의 연락처를 찾을 수 없습니다.")

    def delete_addr(self, name):
        for addr in self.contacts:
            if addr.get_name() == name:
                self.contacts.remove(addr)
                print(f"{name}의 연락처가 삭제되었습니다.")
                return
        print(f"{name}의 연락처를 찾을 수 없습니다.")

    def edit_addr(self, name, new_addr):
        for i, addr in enumerate(self.contacts):
            if addr.get_name() == name:
                self.contacts[i] = new_addr
                print(f"{name}의 연락처가 수정되었습니다.")
                return
        print(f"{name}의 연락처를 찾을 수 없습니다.")