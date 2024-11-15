from Ownerrest import Ownerrest

class Thirdrest(Ownerrest):
    def __init__(self,jjajang,jjampong,pork=12000,dumpling=3000,rice=1000):
        super().__init__(jjajang,jjampong,pork,dumpling,rice)
    def print_price(self,idx=3):
        super().print_price(idx)