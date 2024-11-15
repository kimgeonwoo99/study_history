class Ownerrest:
    def __init__(self,jjajang,jjampong,pork,dumpling,rice):
        self.price_dict = {"짜장":jjajang, "짬뽕":jjampong, "탕수육": pork,"군만두" :dumpling, "공기밥":rice}
 
    def ordin_price(self,key,value):
        print(f"{key} : {value}원 입니다.")

    def print_loc(self,idx):
        print("%d호점 가격표입니다."%idx)

    def print_price(self,idx=0):
        self.print_loc(idx)
        for key, value in self.price_dict.items():
            self.ordin_price(key,value)
        print("="*30)