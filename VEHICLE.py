from abc import ABC, abstractmethod

class VEHICLE(ABC):
    def __init__(self, hangSX, mauxe, namSX):
        self.hangSX = hangSX
        self.mauxe = mauxe 
        self.namSX = namSX

    @abstractmethod
    def __str__(self):
        return f"Hãng sản xuất: {self.hangSX}\n Màu xe: {self.mauxe}\n Năm sản xuất:"
    @abstractmethod
    def tinhtienthue(self):
        pass 
    
   
               

class Oto(VEHICLE):
    def __init__(self, hangSX, mauxe, namSX, socho):
        super().__init__(hangSX, mauxe, namSX)
        self.socho = socho
    def __str__(self):
        return f"Ô tô:\n Hãng sản xuất: {self.hangSX}\n Màu xe: {self.mauxe}\n Năm sản xuất: {self.namSX}\n Số chỗ: {self.socho}\n"
    def tinhtienthue(self):
        return self.socho * 965000
class Moto(VEHICLE):
    def __init__(self, hangSX, mauxe, namSX,  dungtich):
        super().__init__ (hangSX, mauxe, namSX)
        self.dungtich = dungtich
    def __str__(self):
        return f"Mô tô:\n Hãng sản xuất: {self.hangSX}\n Màu xe: {self.mauxe}\n Năm sản xuất: {self.namSX}\n Dung tích: {self.dungtich}\n"
    def tinhtienthue(self):
        return self.dungtich * 23000
class Xetai(VEHICLE):
    def __init__(self, hangSX, mauxe, namSX, taitrong):
        super().__init__ (hangSX, mauxe, namSX)
        self.taitrong = taitrong
    def __str__(self):
        return f"Xe tải:\n Hãng sản xuất: {self.hangSX}\n Màu xe: {self.mauxe}\n Năm sản xuất: {self.namSX}\n Tải trọng: {self.taitrong}\n"
    def tinhtienthue(self):
        return self.taitrong * 3890000


def menu():
    objlist = []
    while True:
        print("=============================MENU===============================")
        print("1.   Ô TÔ")
        print("2.   MÔ TÔ")
        print("3.   XE TẢI")
        print("4.   TÍNH TIỀN THUẾ")
        print("================================================================")

        chon = int(input("YOUR OPTION: "))
        if chon == 0:
            break
        elif chon == 1:
            hangSX = str(input("Nhap hang: "))
            mauxe = str(input("Nhập màu xe: "))
            namSX, socho = map(int, input("Nhập năm sx và số chỗ: ").split())
            ot = Oto(hangSX, mauxe, namSX, socho)
            objlist.append(ot)
        elif chon == 2:
            hangSX = str(input("Nhap hang: "))
            mauxe = str(input("Nhập màu xe: "))
            namSX, dungtich = map(int, input("Nhập năm sx và dung tích: ").split())
            mt = Moto(hangSX, mauxe, namSX, dungtich)
            objlist.append(mt)
        elif chon == 3:
            hangSX = str(input("Nhap hang: "))
            mauxe = str(input("Nhập màu xe: "))
            namSX, taitrong = map(int, input("Nhập năm sx và tải trọng: ").split())
            xt = Xetai(hangSX, mauxe, namSX, taitrong)
            objlist.append(xt)
        elif chon == 4:
            if not objlist:
                    print("Không có xe nào để tính thuế.")
            else:
                for obj in objlist:
                    print(f"{obj}\nTiền thuế: {format(obj.tinhtienthue(), ',.2f')} VND\n")
        else:
            print("Nhập lại: ")
    for obj in objlist:
        print(obj)
menu()



    
    