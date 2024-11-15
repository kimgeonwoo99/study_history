from Ownerrest import Ownerrest

class Firstrest(Ownerrest):
    def __init__(self,jjajang,dumpling,jjampong=8000,pork =12000,rice = 1000):
        super().__init__(jjajang,jjampong,pork,dumpling,rice)
    def print_price(self,idx=1):
        super().print_loc(idx)
        for key, value in self.price_dict.items():
            if key == "군만두":
                print("군만두 : 판매하지 않습니다.")
            else:
                super().ordin_price(key,value)
        print("="*30)
