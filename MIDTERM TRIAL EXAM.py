class Vehicle:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
    def __str__(self):
        return (f"Hãng sản xuất: {self.brand}"
                f"Màu xe: {self.color}"
                f"Năm sản xuất: {self.year}")


class Oto(Vehicle):
    def __init__(self, brand, color, year, seat):
        super().__init__(brand, color, year)
        self.seat = seat
    def __str__(self):
        return f"Ô tô:\n" + super().__str__() + f"\nSố chỗ ngồi: {self.seat}"
    def caculateTAX(self):
        return self.seat * 965000

class Moto(Vehicle):
    def __init__(self, brand, color, year, EngineCapacity):
        super().__init__(brand, color, year)
        self.EngineCapacity = EngineCapacity
    def __str__(self):
        return f"Mô tô: \n" + super().__str__() + f"\nDung tích: {self.EngineCapacity} cc"
    def caculateTAX(self):
        return self.EngineCapacity * 23000

class Truck(Vehicle):
    def __init__(self, brand, color, year, LoadCapacity):
        super().__init__(brand, color, year)
        self.LoadCapacity = LoadCapacity
    def __str__(self):
        return f"Xe tải \n" + super().__str__() + f"\nTải trọng: {self.LoadCapacity} tấn"
    def caculateTAX(self):
        return self.LoadCapacity * 3890000
def main():
    vhc = []
    while True:
        print("===========MENU==============")
        print("1. Ô TÔ")
        print("2. MÔ TÔ")
        print("3. XE TẢI")
        print("4. Hiển thị thông tin các phương tiện")
        print("5.Tính tiền thuế")
        print("6. Thoát")
        print("==============================")
        choice = int(input("Chọn chức năng: "))
        if choice == 1:
            brand = input("Nhập hãng sản xuất: ")
            color = input("Nhập màu xe: ")
            year = input("Nhập năm sản xuất: ")
            seat = input("Nhập số chỗ ngồi: ")
            ot = Oto(brand, color, year, seat)
            vhc.append(ot)
        elif choice == 2:
            brand = input("Nhập hãng sản xuất: ")
            color = input("Nhập màu xe: ")
            year = input("Nhập năm sản xuất: ")
            EngineCapacity = input("Nhập dung tích xilanh :")
            mt = Moto(brand, color, year, EngineCapacity)
            vhc.append(mt)
        elif choice == 3:
            brand = input("Nhập hãng sản xuất: ")
            color = input("Nhập màu xe: ")
            year = input("Nhập năm sản xuất: ")
            Load_Capacity = input("Nhập tải trọng (tấn): ")
            xt = Truck(brand, color, year, Load_Capacity)
            vhc.append(xt)
        elif choice == 4:
            print("\n Thông tin phương tiện  ")
            if len(vhc) == 0:
                print("Chưa có phương tiện nào: ")
            else:
                for xe in vhc:
                    print(xe)
        elif choice == 5:
            print("\n  Bảng tiền thuế   ")
            if len(vhc) == 0:
                print("Chưa có phương tiện nào để tính thuế")
            else:
                for xe in vhc:
                    tax = xe.caculateTAX()
                    print(f"{type(xe).__name__} : {tax:,.3f} VNĐ")
        elif choice == 6:
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại")

if __name__ == "__main__":
    main()



