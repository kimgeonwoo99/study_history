from Address_teacher import Addr

class Addr1(Addr):
    def __init__(self, name, phone, email, address, group, birthday, position):
        super().__init__(name,phone,email,address,group)
        self.__birthday = birthday
        self.__position = position

    def get_birthday(self):
        return self.__birthday
    def set_birthday(self, value):
        self.__birthday = value

    def get_position(self):
        return self.__position
    def set_position(self, value):
        self.__position = value
    
    def print_info(self):
        super().print_info()
        print(f"생일 : {self.get_birthday()}")
        print(f"그룹 (회사 / 거래처) : {self.get_group()}")