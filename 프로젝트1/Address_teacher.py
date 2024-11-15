# Addr 클래스 만들기
class Addr:
    def __init__(self, name, phone, email, address, group):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.__group = group  
    
    # 이름에 대한 getter 와 setter
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value

    # 전화번호에 대한 getter 와 setter
    def get_phone(self):
        return self.__phone
    
    def set_phone(self, value):
        self.__phone = value

    # 이메일에 대한 getter 와 setter
    def get_email(self):
        return self.__email
    
    def set_email(self, value):
        self.__email = value

    # 주소에 대한 getter 와 setter
    def get_address(self):
        return self.__address
    
    def set_address(self, value):
        self.__address = value

    # 그룹에 대한 getter 와 setter
    def get_group(self):
        return self.__group
    
    def set_group(self, value):
        self.__group = value

    # 정보 출력 메소드
    def print_info(self):
        print(f"이름 : {self.get_name()}")
        print(f"전화번호 : {self.get_phone()}")
        print(f"이메일 : {self.get_email()}")
        print(f"주소 : {self.get_address()}")
        # print(f"그룹 (가족 / 친구) : {self.get_group()}")

        