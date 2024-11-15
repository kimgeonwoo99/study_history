from Ownerrest import Ownerrest

class Secondrest(Ownerrest):
    def __init__(self,jjajang,jjampong,pork,rice,dumpling=3000):
        super().__init__(jjajang,jjampong,pork,dumpling,rice)
    def print_price(self,idx=2):
        super().print_loc(idx)
        for key, value in self.price_dict.items():
            if key == "공기밥":
                print("공기밥 : 무료입니다.")
            else:
                super().ordin_price(key,value)
        print("="*30)