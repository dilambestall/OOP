""" Định nghĩa lớp Nguoi có hai lớp con là SinhVien và NhanVien. Trong đó, lớp NhanVien
có hai lớp con NhanVienVanPhong và NhanVienTapVu.
Người có họ tên, ngày sinh, địa chỉ và số điện thoại. Sinh viên có thuộc tính để cho biết
sinh viên đó học ngành nào. Nhân viên có đơn vị và hệ số lương. Nhân viên văn phòng
có chức vụ và nhân viên tạp vụ có công việc. Ghi đè phương thức __str__() trong mỗi
lớp để hiển thị thông tin các thuộc tính của lớp đó.
Viết chương trình kiểm tra bằng cách tạo ba đối tượng của lớp SinhVien,
NhanVienVanPhong và NhanVienTapVu. Sau đó, gọi các phương thức __str__() của
chúng để hiển thị kết quả ra màn hình. Ví dụ:
Nguyễn Văn A, 01/02/2000, 1 Nguyễn Kiệm, 1111, CNTT
Lê Thị B, 03/04/1980, 2 Nguyễn Oanh, 2222, 9,600,000 VND, phòng Kế
Toán, thủ quỹ.
Trần Văn C, 05/06/1970, 3 Quang Trung, 3333, 8,130,000 VND, phòng
Quản Trị, vệ sinh. """



"""class Nguoi:
    def __init__(self, ten, ngaysinh, diachi, sdt):
        self.ten = ten
        self.ngaysinh = ngaysinh
        self.diachi = diachi
        self.sdt = sdt
    def __str__(self):
        return f"{self.ten}    {self.ngaysinh}   {self.diachi}    {self.sdt}"


class SinhVien(Nguoi):
    def  __init__(self, ten, ngaysinh, diachi, sdt, nganhhoc):
        super().__init__(ten, ngaysinh, diachi, sdt )
        self.nganhhoc = nganhhoc
    def __string__(self):
        return super().__str__() + f"{self.nganhhoch}"

class NhanVien(Nguoi):
    def __init__(self,ten ,ngaysinh, diachi, sdt, donvi, hsl):
        super().__init__(ten, ngaysinh, diachi, sdt)
        self.donvi = donvi
        self.hsl = hsl

    def luong(self):
        return self.hsl * 1500000

    def __str__(self):
        return super().__str__() + f"    {self.donvi} , VND  {self.luong()}"

class NhanVienVanPhong(NhanVien):
    def __init__(self, ten, ngaysinh, diachi, sdt, donvi, hsl, chucvu):
        super().__init__(ten, ngaysinh, diachi, sdt, donvi, hsl)
        self.chucvu = chucvu
    def __str__(self):
        return super().__str__() + f" {self.chucvu}"

class NhanVienTapVu(NhanVien):
    def __init__(self,ten ,ngaysinh, diachi, sdt, donvi, hsl, congviec):
        super().__init__(ten ,ngaysinh, diachi, sdt, donvi, hsl)
        self.congviec = congviec
    def __str__(self):
        return super().__str__() + f"   {self.congviec}"

sv = SinhVien("Lâm Phước Dị", "24/12/2004", "1874 Lê Văn Lương", "0879384919", "Khoa Học Dữ Liệu")
print(sv)
nvvp = NhanVienVanPhong("Lâm Phước Huy", "10/3/2003", "8000 Kênh 9 lớn",  "0849", "Marketing", 6.4, "Manager")
print(nvvp)

nvtv =NhanVienTapVu("Lâm Phước Khá", "27/5/2007", "Ca Mau", "0875", "Bo Phan Ky Thuat", 3.2, "Sửa xe")
print(nvtv)"""


class Person:
    def __init__(self, ten, ngaysinh, diachi, sdt):
        self.ten = ten
        self.ngaysinh = ngaysinh
        self.diachi = diachi
        self.sdt = sdt
    def __str__(self):
        return f" {self.ten},    {self.ngaysinh},    {self.diachi},      {self.sdt}"

class Student(Person):
    def __init__(self, ten, ngaysinh, diachi, sdt, nganhhoc):
        super().__init__(ten, ngaysinh, diachi, sdt)
        self.nganhhoc = nganhhoc
    def __str__(self):
        return f" {self.ten},    {self.ngaysinh},    {self.diachi},   {self.sdt},   {self.nganhhoc}"

class Employee(Person):
    def __init__(self, ten, ngaysinh, diachi, sdt, donvi, hsl):
        super().__init__(ten, ngaysinh, diachi, sdt)
        self.donvi = donvi
        self.hsl = hsl
    def luong(self):
        return self.hsl * 1500000
    def __str__(self):
        return super().__str__() + f", {self.donvi},     {self.luong()} VND "

class NhanvienVP(Employee):
    def __init__(self, ten, ngaysinh, diachi, sdt, donvi, hsl,  chucvu):
        super().__init__(ten, ngaysinh, diachi, sdt, donvi, hsl)
        self.chucvu = chucvu
    def __str__(self):
        return super().__str__() + f",   {self.chucvu} "

class NhanvienTV(Employee):
    def __init__(self, ten,ngaysinh, diachi, sdt, hsl, congviec):
        super().__init__(ten, ngaysinh, diachi, sdt, hsl)
        self.congviec = congviec
    def __str__(self):
        return super().__str__() + f",  {self.congviec} "


ten = input("Nhập tên SV: ")
ngaysinh = input("Nhập ngày sinh HV: ")
diachi = input("Nhập địa chỉ HV: ")
sdt = input("Nhập sdt HV: ")
nganhhoc = input("Nhập ngành học HV: ")
st = Student(ten, ngaysinh, diachi, sdt, nganhhoc)
print(st)


ten = input("Nhập tên NV: ")
ngaysinh = input("Nhập ngày sinh NV: ")
diachi = input("Nhập địa chỉ NV: ")
sdt = input("Nhập sdt NV: ")
donvi = input("Nhập đơn vị NV")
hsl = int(input("Nhập hệ số lương: "))
chucvu = input("Nhập chức vụ nhân viên: ")
nvvp = NhanvienVP(ten, ngaysinh, diachi, sdt, donvi, hsl, chucvu)
print(nvvp)

congviec = input("Nhập công việc NV: ")
nvtv = NhanvienVP(ten, ngaysinh, diachi, sdt, donvi,hsl, congviec)
print(nvtv)

