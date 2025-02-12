
"""def Caculator():
    while True:
        try:
            number1 = int(input("Nhập số  thứ nhất: "))
            number2 = int(input("Nhập số thứ hai: "))
        except (ValueError, IndexError):
            print("Số không hợp lệ, vui lòng nhập một số hợp lệ!")
            continue

        print("Các phép tính: ")
        print("1. Cộng(+)")
        print("2. Trừ(-)")
        print("3. Nhân(x)")
        print("4. Chia(/)")
        print("\n")


        operation = input("Chọn phép tính: ")
        match operation:
            case "1" | "+":
                result = number1 + number2
                print(f"{number1} + {number2} = {result}")

            case "2" | "-":
                result = number1 - number2
                print(f"{number1} - {number2} = {result}")

            case "3" | "*" | "x":
                result = number1 * number2
                print(f"{number1} x {number2} = {result}")

            case "4" | "/" | ":":
                if number2 == 0:
                    print("Lỗi xác định")
                else:
                    result = number1 / number2
                    print(f"{number1} / {number2} = {result}")

            case _:
                print("Lựa chọn không hợp lệ vui lòng chọn lại:")


        repeat = input("Bạn có muốn thực hiện một phép tính khác không(c/k): ").lower()
        if repeat != "c":
            break

Caculator()"""

