from abc import ABC, abstractmethod

class NhanVien(ABC):
    def __init__(self, ho, ten, id):
        self.ho = ho
        self.ten = ten
        self.id = id

    @abstractmethod
    def thuNhap(self):
        pass

class NHANVIENCONGNHAT(NhanVien):
    def __init__(self, ho, ten, id, luongtuan):
        super().__init__(ho, ten, id)
        self.luongtuan = luongtuan

    def thuNhap(self):
        return self.luongtuan * 100

    def __str__(self):
        return f"Nhân viên công nhật: \n{self.ho} {self.ten}\nSố CCCD: {self.id}\nLương tuần: {self.luongtuan}\nTổng cộng: {self.thuNhap()}"

class NHANVIENLAMGIO(NhanVien):
    def __init__(self, ho, ten, id, luongGio, soGio):
        super().__init__(ho, ten, id)
        self.luongGio = luongGio
        self.soGio = soGio

    def thuNhap(self):
        if self.soGio <= 40:
            return self.soGio * self.luongGio
        else:
            return (self.luongGio * 40) + (self.soGio - 40) * 1.5 * self.luongGio

    def __str__(self):
        return f"Nhân viên làm giờ: \n{self.ho} {self.ten}\nSố CCCD: {self.id}\nLương giờ: {self.luongGio}\nSố giờ: {self.soGio}\nTổng cộng: {self.thuNhap()}"

def menu():
    objlist = []
    while True:
        print("================================MENU===================================")
        print("1. Nhân viên công nhật")
        print("2. Nhân viên làm giờ")
        print("3. Thoát")
        chon = int(input("Your option: "))
        if chon == 3:
            break
        elif chon == 1:
            ho = input("Nhập họ: ")
            ten = input("Nhập tên: ")
            id, luongtuan = map(int, input("Nhập CCCD, lương tuần: ").split())
            nvcn = NHANVIENCONGNHAT(ho, ten, id, luongtuan)
            objlist.append(nvcn)
        elif chon == 2:
            ho = input("Nhập họ: ")
            ten = input("Nhập tên: ")
            id, luonggio, sogio = map(int, input("Nhập CCCD, lương giờ, số giờ: ").split())
            nvlg = NHANVIENLAMGIO(ho, ten, id, luonggio, sogio)
            objlist.append(nvlg)
        else:
            print("Nhập lại: ")

    for obj in objlist:
        print(obj)

menu()
