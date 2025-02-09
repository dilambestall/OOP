""" Yêu cầu: Lớp TaiKhoan có các thành phần sau:
- Dữ liệu kiểu số nguyên là soTK để chứa số tài khoản, trị mặc định là 0. Dữ liệu kiểu
số thực là soDu để chứa số dư của tiền gửi, trị mặc định là 0. Dữ liệu kiểu số thực là
laiSuatNam để chứa lãi suất hằng năm (tính theo phần trăm, ví dụ 6.5 %), trị mặc
định là 0. Giả sử tất cả tài khoản có cùng lãi suất. Dữ liệu kiểu ngày tháng là ngayTao
để chứa ngày tạo tài khoản.
- Phương thức tạo dựng không đối số để tạo tài khoản mặc định với ngày tạo tài khoản
là ngày hiện tại của hệ thống. Phương thức tạo dựng có đối số để tạo tài khoản với
số tài khoản và số dư có giá trị được chỉ định.
- Phương thức getter cho ngayTao để trả về chuỗi chứa ngày tháng theo dạng
"dd/mm/yyyy". Phương thức setter cho laiSuatNam để thiết lập lãi suất hằng năm.
LTHĐT: Câu Hỏi & Bài Tập Chương 3 ThS. GVC. Tô Oai Hùng
5
Phương thức tienLaiThang() trả về tiền lãi hằng tháng (tiền lãi tháng = số dư ×
lãi suất năm / 12 / 100) .
- Phương thức rutTien() để rút số tiền được chỉ định từ tài khoản. Phương thức
guiTien() để gửi số tiền được chỉ định vào tài khoản.
• Lớp TaiKhoanSec thừa kế từ lớp TaiKhoan. Lớp này có các thành phần sau:
- Dữ liệu kiểu số thực là chiTroi dùng để chứa số tiền mà chủ tài khoản được phép
rút không vượt quá tổng số dư với số tiền này.
- Phương thức tạo dựng để tạo tài khoản séc với số tài khoản và số dư có giá trị được
chỉ định. Phương thức setter cho thuộc tính chiTroi.
- Ghi đè phương thức của lớp cha để số tiền rút không vượt quá tổng số dư với số tiền
được phép chi trội.
- Ghi đè các phương thức khác (nếu cần).
• Lớp TaiKhoanTietKiem thừa kế từ lớp TaiKhoan. Lớp này có các thành phần dữ liệu
và phương thức sau:
- Phương thức tạo dựng để tạo tài khoản tiết kiệm với số tài khoản và số dư có giá trị
được chỉ định.
- Ghi đè phương thức của lớp cha để số tiền rút không vượt quá số dư. Ghi đè các
phương thức khác (nếu cần).
a) Viết chương trình kiểm tra bằng cách tạo đối tượng của lớp TaiKhoanSec và
TaiKhoanTietKiem như sau:
- Đối tượng TaiKhoanSec: Số tài khoản là 123, số dư là $10,000, lãi suất hằng năm
là 6.5% và số tiền chi trội tối đa là $1,000. Lúc đầu gửi $3,000, sau đó rút $11,000.
Hãy hiển thị số tài khoản, số dư, tiền lãi hằng tháng (hoặc tiền phải trả lãi) có hai số
lẻ và ngày tạo tài khoản. Ví dụ:
Tài khoản séc:
Số tài khoản: 123
Số dư: $2000.00
Lãi hằng tháng: $10.83
Ngày tạo: 13/10/2018
- Đối tượng TaiKhoanTietKiem: Số tài khoản là 456, số dư là $20,000 và lãi suất
hằng năm là 5.5%. Lúc đầu gửi $2,000, sau đó rút $2,500. Hãy hiển thị số tài
khoản, số dư, tiền lãi hằng tháng có hai số lẻ và ngày tạo tài khoản.
b) Thực hiện lại câu a) với số tiền rút trong đối tượng TaiKhoan-Sec là $13,500 và số
tiền rút trong đối tượng TaiKhoanTiet-Kiem là $25,000.  """

from datetime import datetime
class Taikhoan:
    laisuatnam = 0
    def __init__(self, soTK = 0, soDu = 0):
        self.soTK = soTK
        self.soDu = soDu
        self.ngaytao = datetime.now()
    def get_ngaytao(self):
        return self.ngaytao.strftime("%d/%m/%Y")
    @classmethod
    def set_LaiSuatNam(cls, laisuat):
        cls.laisuatnam = laisuat

    def tienLaiThang(self):
        if self.soDu < 0:  # Nếu số dư âm, tính lãi trên số dư âm
            return round(abs(self.soDu) * Taikhoan.laisuatnam / 12 / 100, 2)
        return round(self.soDu * Taikhoan.laisuatnam / 12 / 100, 2)

    def ruttien(self, soTien):
        if soTien > self.soDu:
            raise ValueError("Số tiền rút vượt quá số  dư tài khoản!  ")
        self.soDu -= soTien
    def guitien(self, soTien):
        self.soDu += soTien


class taikhoanSec(Taikhoan):
    def __init__(self, soTK = 0, soDu = 0, chiTroi = 0):
        super().__init__(soTK, soDu)
        self.chiTroi = chiTroi
    def set_chiTroi(self, chiTroi):
        self.chiTroi = chiTroi
    def ruttien(self, soTien):
        if soTien > self.soDu + self.chiTroi:
            raise ValueError("Số tiền rút vượt quá số dư và hạn mức chi trội: ")
        self.soDu -= soTien


class taikhoanTietkiem(Taikhoan):
    def __init__(self, soTK = 0, soDu = 0, soDutoithieu = 500):
        super().__init__(soTK, soDu)
        self.soDutoithieu = soDutoithieu
        self.solanruttrongthang = 0
        self.gioihanrut = 3 # giới hạn số lần rút trong tháng
    def ruttien(self, soTien):
        if self.solanruttrongthang > self.gioihanrut:
            print("Rút thất bại! Số lần rút trong tháng vượt quá", self.gioihanrut, " lần!")
            return
        elif soTien > self.soDu - self.soDutoithieu:
            print("Không thể rút vì nó đã vượt quá số tiền bạn tiết kiệm: ")
            return
        self.soDu -= soTien
        self.solanruttrongthang += 1
        print(f"Đã rút: ${soTien:.3f}. Số dư còn lại:  ${self.soDu:.3f}.")
if __name__ ==  "__main__":

    # TÀI KHOẢN SEC
    tks = taikhoanSec(123, 10000, 1000)
    Taikhoan.set_LaiSuatNam(6.5)
    tks.guitien(3000)
    try:
        tks.ruttien(13500)
    except ValueError as d:
        print(d)
        print("Vui lòng kiểm tra lại hay bạn hãy liên hê ngân hàng để nâng mức chi trội")
    print("Tài khoản SEC:")
    print(f"Số tài khoản: {tks.soTK}")
    print(f"Số dư: {tks.soDu:.3f}")
    if tks.soDu < 0:
        print(f"Trả lãi ngân hàng: ${tks.tienLaiThang():.3f}")
    else:
        print(f"Lãi hằng tháng: ${tks.tienLaiThang():.3f}")
    print(f"Ngày tạo: {tks.get_ngaytao()}")

    # TÀI KHOẢN TIẾT KIỆM
    tktk = taikhoanTietkiem(456, 20000, 500)
    Taikhoan.set_LaiSuatNam(5.5)
    tktk.guitien(2000)
    tktk.ruttien(25000)
    print("\nTài khoản tiết kiệm")
    print(f"Số tài khoản: {tktk.soTK}")
    print(f"Số dư: ${tktk.soDu:.3f}")
    print(f"Lãi hàng tháng: ${tktk.tienLaiThang():.3f}")
    print(f"Ngày tạo: {tktk.get_ngaytao()}")





