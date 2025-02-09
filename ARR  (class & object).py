class PhanTuLonNhat:
    def __init__(self, hang, cot, gia_tri):
        self.hang = hang
        self.cot = cot
        self.gia_tri = gia_tri
        self.arr = []

    def nhap_mang(self):
        for i in range(self.hang):
            row = []
            for j in range(self.cot):
                print(f"Nhập phần tử tại vi")



    def tim_phan_tu_lon_nhat(self):
        max_value = self.arr[0][0]
        max_row = 0
        max_col = 0
        for i in range(self.hang):
            for j in range(self.cot):
                if self.arr[i][j] > max_value:
                    max_value = self.arr[i][j]
                    max_row = i
                    max_col = j
        self.gia_tri = max_value
        self.hang = max_row
        self.cot = max_col

    def trave(self):
        print(f"Phần tử lớn nhất là {self.gia_tri} ở vị trí ({self.hang}, {self.cot})")

# Sử dụng lớp
hang = int(input("Nhập số hàng: "))
cot = int(input("Nhập số cột: "))

mang = PhanTuLonNhat(hang, cot, None)
mang.nhap_mang()
mang.tim_phan_tu_lon_nhat()
mang.trave()
