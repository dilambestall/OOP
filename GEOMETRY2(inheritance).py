""" Yêu cầu: Lớp HinhChuNhat thừa kế từ lớp HinhHoc. Lớp này có:
- Hai thành phần dữ liệu kiểu số thực để chứa giá trị của chiều dài và chiều rộng hình
chữ nhật.
- Phương thức tạo dựng có đối số để tạo hình chữ nhật với chiều dài và rộng có giá
trị được chỉ định.
- Phương thức tinhDienTich() và tinhChuVi() để trả về diện tích và chu vi của
hình chữ nhật.
- Phương thức __str__() để trả về chuỗi mô tả hình chữ nhật (hoặc hình vuông) bao
gồm: Tên, tọa độ tâm, giá trị chiều dài và chiều rộng (hoặc cạnh nếu là hình vuông),
diện tích và chu vi của hình chữ nhật.
• Lớp HinhVuong thừa kế từ lớp HinhChuNhat. Lớp này có duy nhất phương thức tạo
dựng có đối số để tạo hình vuông với cạnh có giá trị được chỉ định. Biết rằng, hình
vuông là hình chữ nhật khi chiều dài bằng chiều rộng.
• Lớp Ellipse thừa kế từ lớp HinhHoc. Lớp này có:
- Hai thành phần dữ liệu kiểu số thực để chứa giá trị của ½ trục lớn và ½ trục bé.
- Phương thức tạo dựng có đối số để tạo hình ellipse với các thành phần dữ liệu có
giá trị được chỉ định.
- Phương thức tinhDienTich() và tinhChuVi() để trả về diện tích và chu vi của
hình ellipse.
- Phương thức __str__() để trả về chuỗi mô tả hình ellipse (hoặc hình tròn) bao
gồm: Tên, tọa độ tâm, giá trị cạnh a và b (hoặc bán kính nếu là hình tròn), diện tích
và chu vi của hình ellipse.
• Lớp HinhTron thừa kế từ lớp Ellipse. Lớp này có duy nhất phương thức tạo dựng có
đối số để tạo hình tròn với bán kính có giá trị được chỉ định. Biết rằng, hình tròn là
hình ellipse khi hai trục bằng nhau.
Viết chương trình kiểm tra bằng cách hiển thị menu để người sử dụng chọn loại hình cần
thao tác, sau đó nhập và hiển thị kết quả (diện tích và chu vi lấy 2 số lẻ). Quá trình lặp lại
cho đến khi mục "Thoát" được chọn. """

from math import *
class Hinhhoc:
    def __init__(self, ten, x, y):
        self.ten = ten
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.ten}   Tọa độ: ({self.x}, {self.y})"
class Hinhchunhat(Hinhhoc):
    def __init__(self, ten, x, y, dai, rong):
        super().__init__(ten, x, y)
        self.dai = dai
        self.rong = rong
    def tinhCV(self):
        return (self.dai + self.rong) * 2
    def tinhDT(self):
        return self.dai * self.rong
    def __str__(self):
        if self.dai == self.rong:
            self.ten = "Hình chữ nhật"

        else:
            self.ten = "Hình vuông"
        return (f" {self.ten}  Tọa độ: ({self.x}, {self.y}) \n"
                f"Chu vi: {self.tinhCV()}\n"
                f"Diện tích: {self.tinhDT()}")
class Hinhvuong(Hinhchunhat):
    def __init__(self, ten, x, y, canh):
        super().__init__(ten, x, y, dai = canh, rong = canh)


class Ellipse(Hinhhoc):
    def __init__(self, ten, x, y, a, b):
        super().__init__(ten, x, y)
        self.a = a
        self.b = b
    def tinhCV(self):
        return round(pi * (self.a + self.b))

    def tinhDT(self):
        return round(pi * (self.a * self.b))

    def __str__(self):
        if self.a == self.b:
            self.ten = "Hình tròn"
        else:
            self.ten = "Hình Ellipse"
        return (f"{self.ten}      Tọa độ: ({self.x}, {self.y})  "
                f"Chu vi:  {self.tinhCV()}  "
                f"Diện tích:  {self.tinhDT()}  ")
class Hinhtron(Ellipse):
    def __init__(self,ten , x, y, r):
        super().__init__(ten, x, y, a = r, b = r )


def menu():
    while True:
        option = int(input("0. Thoát    1. Hình chữ nhật      2. Hình vuông      3. Hình Ellipse      4. Hình tròn \n"))
        if option == 1:
            ten = ""
            x, y = map(int, input("Nhập tọa độ x, y: ").split())
            dai, rong = map(int, input("Nhập chiều dài, rộng: ").split())
            hcn = Hinhchunhat(ten, x, y, dai, rong)
            print(hcn)
        elif option == 2:
            ten = ""
            x, y = map(int, input("Nhập tọa độ x, y: ").split())
            canh = int(input("Nhập độ dài cạnh hình vuông: "))
            hv = Hinhvuong(ten, x, y, canh)
            print(hv)
        elif option == 3:
            ten = ""
            x, y = map(int, input("Nhập tọa độ x, y: ").split())
            a, b = map(int, input("Nhập độ dài trục lớn trục bé: ").split())
            el = Ellipse(ten, x, y, a, b)
            print(el)
        elif option == 4:
            ten = ""
            x, y = map(int, input("Nhập tọa độ x, y: ").split())
            r = int(input("Nhập bán kính: "))
            ht = Hinhtron(ten, x, y, r)
            print(ht)
        elif option == 0:
            break
menu()














