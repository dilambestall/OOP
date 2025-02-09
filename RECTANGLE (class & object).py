''' Yêu cầu: Định nghĩa lớp có tên là HinhChuNhat để thể hiện cho hình chữ nhật. Lớp này có:
- Hai thành phần dữ liệu là dai và rong dùng để chứa giá trị của chiều dài và chiều
rộng hình chữ nhật. Giá trị mặc định của chúng là 1.0.
- Phương thức tạo dựng không đối số để tạo hình chữ nhật với các giá trị mặc định.
- Phương thức tạo dựng để tạo hình chữ nhật với dai và rong có giá trị được chỉ định.
- Phương thức tinhDienTich() để trả về diện tích của hình chữ nhật.
- Phương thức tinhChuVi() để trả về chu vi của hình chữ nhật.
- Thêm các phương thức khác (nếu cần).
a) Tạo đối tượng HinhChuNhat có chiều dài và chiều rộng với giá trị mặc định. Hiển
thị chiều dài, chiều rộng, diện tích và chu vi của hình chữ nhật theo thứ tự đã nêu.
b) Tạo đối tượng HinhChuNhat có chiều dài là 5.5 và chiều rộng là 4.5. Hiển thị các
thông tin của hình chữ nhật như câu (a).
c) Tạo đối tượng HinhChuNhat có chiều dài và rộng được nhập từ bàn phím. Hiển thị
các thông tin của hình chữ nhật đã nhập như câu (a). '''

class HinhChuNhat:
    def __init__(self, dai = 1.0, rong = 1.0):
        self.dai = dai
        self.rong = rong
    def tinhCV(self):
        return (self.dai + self.rong) * 2
    def tinhDT(self):
        return self.dai * self.rong
    def Hienthi(self):
        print(f"D = {self.dai}  R = {self.rong}  CV = {self.tinhCV()}  DT = {self.tinhDT()} ")

    def __str__(self):
        return f" D = {self.dai}  R = {self.rong}  CV = {self.tinhCV()}    DT = {self.tinhDT()} "


"HCN với chiều dài và chiều rộng có giá trị mặc định "
hcn1 = HinhChuNhat()
hcn1.Hienthi()



"HCN với d = 5.5 và r = 4.5"
hcn2 = HinhChuNhat(5.5, 4.5)
print(hcn2)



"HCN có chiều  dài và chiều  rộng nhập từ bàn phím"
d, r = map(int, input("Nhập lần lượt chiều dài và chiều rộng của HCN:").split())
hcn3 = HinhChuNhat(d, r)
hcn3.Hienthi()




