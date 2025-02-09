"""Định nghĩa các lớp theo các yêu cầu sau:
• Lớp HinhHoc có các thành phần dữ liệu và phương thức sau:
- Dữ liệu là ten (chuỗi) để chứa tên của mỗi loại hình.
- Dữ liệu là x và y (số nguyên) để chứa hoành độ và tung độ tâm của hình.
- Các phương thức setter hoặc constructor cho các thành phần dữ liệu.
- Phương thức __str__() trả về chuỗi mô tả thông tin chung về các loại hình theo
dạng: "<ten>: Tọa độ (<x>, <y>)".
• Lớp TamGiac thừa kế từ lớp HinhHoc. Lớp này có:
- Các thành phần dữ liệu kiểu số thực để chứa giá trị của ba cạnh tam giác.
- Phương thức tạo dựng có đối số để tạo tam giác với ba cạnh có giá trị được chỉ định.
- Phương thức tinhDienTich() trả về diện tích của tam giác.
- Phương thức tinhChuVi() trả về chu vi của tam giác.
- Phương thức __str__() trả về chuỗi mô tả tam giác: "<ten>: Tọa độ (<x>, <y>), a = <a>, b = <b>, c = <c

Viết chương trình kiểm tra để nhắc người sử dụng nhập tọa độ tâm và ba cạnh của
tam giác. Sau đó, hiển thị chuỗi bao gồm tên, tọa độ tâm, giá trị ba cạnh, diện tích và
chu vi của tam giác.

Mở rộng câu trên bằng cách thêm phương thức xacDinhTamGiac() vào lớp chính để
thực hiện các yêu cầu sau dựa vào ba cạnh của tam giác:
- Kiểm tra sự tồn tại của tam giác.
- Nếu là tam giác, chương trình sẽ xác định là tam giác gì. Giả sử chỉ có các loại tam
giác sau: Tam giác đều, cân, vuông và thường  """


from math import *
class Hinhhoc:
    def __init__(self, ten, x, y):
        self.ten = ten
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.ten}    Tọa độ: ({self.x}, {self.y})"

class TamGiac(Hinhhoc):
    def __init__(self, ten, x, y, a, b, c):
        super().__init__(ten, x, y)
        self.a = a
        self.b = b
        self.c = c
    def tinhCV(self):
        return self.a + self.b + self.c
    def tinhDT(self):
        p = self.tinhCV() / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    def xacDinhTamGiac(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            if self.a == self.b == self.c:
                self.ten = "Tam giác đều"
            elif self.a == self.b or self.a == self.c or self.b == self.c:
                self.ten = " Tam giác cân "
            elif (self.a ** 2 + self.b ** 2 == self.c ** 2 or
                  self.a ** 2 + self.c ** 2 == self.b ** 2 or
                  self.b ** 2 + self.c ** 2 == self.a ** 2):
                self.ten = " Tam giác vuông"
            else:
                self.ten = " Tam giác thường"
            print(self)

        else:
            print("Đây không phải là tam giác:")


    def __str__(self):
        return f"{self.ten}     Tọa độ: ({self.a}, {self.b})   a = {self.a}  b = {self.b}   c = {self.c}    Chu vi: {self.tinhCV()}   Diện tích: {self.tinhDT()}"


if __name__ == "__main__":
    ten = "Tam giác"
    x = int(input("Nhập toạ độ tâm x: "))
    y = int(input("Nhập tọa độ tâm y: "))
    a, b, c = map(int, input("Nhập cạnh a, b, c: ").split())
    tg = TamGiac(ten, x, y, a, b, c)
    print(tg)
    tg.xacDinhTamGiac()



