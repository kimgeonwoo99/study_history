from OwnerRest import OwnerRest
from FirstRest import FirstRest
from SecondRest import SecondRest
from ThirdRest import ThirdRest

if __name__ == "__main__":
    a = OwnerRest(8000, 8000, 12000, 3000, 1000)
    a.print_price()
    b = FirstRest(7000, 0)
    b.print_price()
    c = SecondRest(5000, 5000, 10000, 0)
    c.print_price()
    d = ThirdRest(7000, 7000)
    d.print_price()
