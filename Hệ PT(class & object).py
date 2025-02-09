""" Định nghĩa lớp có tên là HePhuongTrinh để thể hiện cho hệ phương trình tuyến tính bậc
nhất hai ẩn số:
ax + by = e
cx + dy = f
- Các thành phần dữ liệu là a, b, c, d, e và f dùng để chứa giá trị của các hệ số.
- Phương thức tạo dựng để khởi tạo trị cho các thành phần dữ liệu.
- Phương thức isLoiGiai() trả về true nếu ad – bc khác 0.
- Các phương thức getX() và getY() để trả về nghiệm x và y của hệ phương trình.
Viết chương trình kiểm tra nhắc người sử dụng nhập giá trị cho các hệ số. Nếu ad – bc
khác 0, hiển thị nghiệm x và y (lấy 2 số lẻ). Ngược lại, hiển thị "Hệ phương trình vô
nghiệm. """


class HPT:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    def mau(self):
        return self.a * self.d - self.b * self.c
    def isLoigiai(self):
        return self.mau() != 0
    def getX(self):
        return (self.d * self.e - self.b * self.f) / self.mau()
    def getY(self):
        return (self.a * self.f - self.c * self.e) / self.mau()
    def Hienthinghiem(self):
        if self.isLoigiai():
            print(f"X = {self.getX()}    Y = {self.getY()}")
        else:
            print("Phương trình vô nghiệm: ")

a, b, c, d, e , f = map(int, input("Nhập a -> f: ").split())
hpt = HPT(a, b, c, d, e, f)
hpt.Hienthinghiem()



