from OwnerRest import OwnerRest

class SecondRest(OwnerRest):
    def __init__(self,jjajang,jjampong,pork,rice,dumpling=3000):
        super().__init__(jjajang,jjampong,pork,dumpling,rice)
    def print_price(self,idx=2):
        super().print_loc(idx)
        for item, price in self.price_dict.items():
            if item == "공기밥":
                print("공기밥 : 무료입니다.")
            else:
                super().ordin_price(item, price)
        print("="*30)
