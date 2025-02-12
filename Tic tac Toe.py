def displayBoard(board):
    size = len(board)
    for i in range(size):
        for j in range(size):
            if j < size - 1:
                print(f" {board[i][j]}", end = "|")
            else:
                print(f" {board[i][j]}", end = "|")
        print()
        if i < size - 1:
            print("-" * (size * 4 - 1))

def checkWinner(board):
    size = len(board)
    for i in range(size):
        if all(board[i][j] == board[i][0] != ' ' for j in range(size)):
            return board[i][0]

    for j in range(size):
        if all(board[i][j] == board[0][j] != ' ' for i in range(size)):
            return board[0][j]

    if all(board[i][i] == board[0][0] != ' ' for i in range(size)):
        return board[0][0]
    if all(board[0][size - 1] == board[i][size - i - 1] != ' ' for i in range(size)):
        return board[0][size - 1]


    return None


def isDraw(board):
    return all(j != ' ' for i in board for j in i)


def main():
    while True:
        try:
            size = int(input("Enter the size of the Board(3, 4, 5 for  3x3, 4x4 , 5x5 respectively): "))
            if size not in [3, 4, 5]:
                print("Kích cỡ không hợp lệ, vui lòng nhập 3, 4 or 5")
                continue # Quay trở lại nhập giá trị
            break # dừng vòng lặp chuyển sang phàn tiếp theo
        except ValueError:
            print("Số không hợp lệ, vui lòng nhập vào số nguyên:")


    board = [[' ' for _ in range(size)] for _ in range(size)]
    currentPlayer = 'X'
    while True:
        displayBoard(board)
        print(f"Player  {currentPlayer}, make your move(row col): ")
        try:
            row, col = map(int, input().split())
            if not ((row >= 0 and row < size) and (col >= 0 and col < size)):
                print(f"Đầu vào không hợp lệ, hàng và cột cần phải nằm(0, size -1). ")
                continue
            if board[row][col] != ' ':
                print("Ô đã được đánh dấu, thử lại")
                continue
            board[row][col] = currentPlayer

            winner = checkWinner(board)
            if winner:
                displayBoard(board)
                print(f"Player {winner} win!")
            if isDraw(board):
                displayBoard(board)
                print("It is Tie")
                break

            currentPlayer = 'O' if currentPlayer == 'X' else 'X'


        except (ValueError, IndexError):
            print("Invalid input. Please enter row, col as integers within range.")

if __name__ == "__main__":
    main()





