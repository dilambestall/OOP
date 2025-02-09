'''Định nghĩa lớp có tên là DaGiacDeu để thể hiện cho đa giác đều. Lớp này có:
- Thành phần dữ liệu là n để chứa số cạnh của đa giác với giá trị mặc định là 3.
- Thành phần dữ liệu là canh dùng để chứa chiều dài của mỗi cạnh (các cạnh bằng
nhau) với giá trị mặc định là 1.0.
- Hai thành phần dữ liệu là x và y để chứa hoành độ và tung độ tâm của đa giác với
giá trị mặc định là 0.
- Phương thức tạo dựng không đối số để tạo đa giác đều với các giá trị mặc định.
- Phương thức tạo dựng để tạo đa giác đều với số cạnh, chiều dài cạnh, hoành độ và
tung độ tâm của đa giác có giá trị được chỉ định.
- Phương thức tinhDienTich() để trả về chu  vi và diện tích của đa giác'''


from math import *
class Dagiacdeu:
    def __init__(self, n = 3, canh = 1.0, x = 0, y = 0):
        self.n = n
        self.canh = canh
        self.x = x
        self.y = y
    def tinhCV(self):
        return self.n * self.canh
    def tinhDT(self):
        return (self.n * pow(self.canh, 2)) / (4 * tan(pi / self.n))
    def __str__(self):
        return f"So canh: {self.n}   Do dai = {self.canh}   Tọa độ: ({self.x}, {self.y})"


"Đa giác đều với các giá trị mặc định"
polygon1 = Dagiacdeu()
print(polygon1)

"Đa giác đều với các trị được chỉ định"
polygon2 = Dagiacdeu(6, 4, 1, 2)
print(polygon2)

"Đa giác đều với giá trị nhập từ bàn phím"
n, canh, x, y = map(float, input("Nhập n, canh, x, y: ").split())
polygon3 = Dagiacdeu(n, canh, x, y)
print(polygon3)













