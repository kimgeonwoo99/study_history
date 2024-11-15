from Ownerrest import Ownerrest
from Firstrest import Firstrest
from Secondrest import Secondrest
from Thirdrest import Thirdrest

if __name__ == "__main__":
    a = Ownerrest(8000, 8000, 12000, 3000, 1000)
    a.print_price()
    b = Firstrest(7000, 0)
    b.print_price()
    c = Secondrest(5000, 5000, 10000, 0)
    c.print_price()
    d = Thirdrest(7000, 7000)
    d.print_price()