class HoTen:
    def __init__(self, ho, lot, ten):
        self.ho = ho
        self.lot = lot
        self.ten = ten

    def getname(self):
        return self.ho + ' ' + self.lot + ' ' + self.ten


class Diachi:
    def __init__(self, diachi):
        self.address = diachi


class SinhVien:
    def __init__(self, ten):
        tmp = ten.split()
        self.ten = HoTen(tmp[0], tmp[1], tmp[2])  # Tạo đối tượng HoTen với họ, lót và tên
        self.diachilist = []

    def addaddress(self, diachi):
        self.diachilist.append(diachi)

    def getaddaddress(self):
        return [i.address for i in self.diachilist]  # Lấy địa chỉ từ các đối tượng Diachi

    def getname(self):
        return self.ten.getname()  # Gọi getname từ đối tượng HoTen


# Tạo đối tượng SinhVien và Diachi, sau đó in ra kết quả
sv = SinhVien('Nguyễn Văn A')
dc1 = Diachi('1 Nguyên Kiệm')
dc2 = Diachi('2 Nguyễn Oanh')
sv.addaddress(dc1)
sv.addaddress(dc2)

print("Tên sinh viên:", sv.getname())
print("Địa chỉ sinh viên:", sv.getaddaddress())
