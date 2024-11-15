from OwnerRest import OwnerRest

class FirstRest(OwnerRest):
    def __init__(self,jjajang,dumpling,jjampong=8000,pork =12000,rice = 1000):
        super().__init__(jjajang,jjampong,pork,dumpling,rice)
    def print_price(self,idx=1):
        super().print_loc(idx)
        for item, price in self.price_dict.items():
            if item == "군만두":
                print("군만두 : 판매하지 않습니다.")
            else:
                super().ordin_price(item, price)
        print("="*30)
