"""class Phanso:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def USCLN(self, a, b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

    def toigian(self):
        usc = self.USCLN(self.tu, self.mau)
        self.tu = int(self.tu / usc)
        self.mau = int(self.mau / usc)



    def __add__(self, other):
        tumoi = self.tu * other.mau + self.mau * other.tu
        maumoi = self.mau * other.mau
        k = Phanso(tumoi, maumoi)
        k.toigian()
        return k
    def __sub__(self, other):
        tumoi = self.tu * other.mau - self.mau * other.tu
        maumoi = self.mau * other.mau
        k = Phanso(tumoi, maumoi)
        k.toigian()
        return k
    def __mul__(self, other):
        tumoi = self.tu * other.tu
        maumoi = self.mau * other.mau
        k =Phanso()
        k.toigian()





tu1 = int(input("Tử số của phân số thứ 1: "))
while True:
    mau1 = int(input("Nhập mẫu của phân số của phân số thứ nhất: "))
    if mau1 != 0:
        break

tu2 = int(input("Nhập tử của phân số thứ 2: "))
while True:
    mau2 = int(input("Nhập mẫu số của phân số thứ 2: "))
    if mau2 != 0:
        break

ps1 = Phanso(tu1, mau1)
ps2 = Phanso(tu2, mau2)
cong = ps1 + ps2
tru = ps1 - ps2
#nhan = ps1 * ps2
#chia = ps1 * ps2
print(f"{ps1.tu}/ {ps1.mau} + {ps2.tu}/{ps2.mau} ={cong.tu} / {cong.mau} ")
print(f"{ps1.tu}/ {ps1.mau} -  {ps2.tu}/{ps2.mau} ={tru.tu} / {tru.mau} ")"""


class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def USCLN(self, a , b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return a
    def toigian(self):
        usc = self.USCLN(self.tu, self.mau)
        self.tu = int(self.tu / usc)
        self.mau = int(self.mau / usc)
    def __add__(self, other):
        tumoi = self.tu * other.mau + self.mau * other.tu
        maumoi = self.mau * other.mau
        k = PhanSo(tumoi, maumoi)
        k.toigian()
        return k
    def __sub__(self, other):
        tumoi = self.tu * other.mau - self.mau * other.tu
        maumoi = self.mau * other.mau
        k = PhanSo(tumoi, maumoi)
        k.toigian()
        return k
tu1 = int(input("Nhập tử số của phân số thứ 1: "))
while True:
    mau1 = int(input("Nhập mẫu số của phân số thứ 1: "))
    if mau1 != 0:
        break
tu2 = int(input("Nhập tử số của phân số thứ 2:"))
while True:
    mau2 = int(input("Nhập mẫu số của phân số thứ 2: "))
    if mau2 != 0:
        break

ps1 = PhanSo(tu1, mau1)
ps2 = PhanSo(tu2, mau2)
cong = ps1 + ps2
tru = ps1 - ps2
print(f"{ps1.tu} / {ps1.mau} + {ps2.tu} / {ps2.mau} = {cong.tu} / {cong.mau}")
print(f"{ps1.tu} / {ps1.mau} - {ps2.tu} / {ps2.mau} = {tru.tu} / {tru.mau}")
