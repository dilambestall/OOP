import random

def getComputerOption():
    return random.choice([1, 2, 3])

def getPlayeroption():
    while True:
        try:
            option = int(input("Your option is:  1(Búa) or 2(Bao) or 3(Kéo): "))
            if option in [1, 2, 3]:
                return option
        except ValueError:
            print("Lựa chọn cảu bạn không hợp lệ, vui lòng chọn 1, 2 or 3.")
def determineWinner(PlayerOption, ComputerOption):
    if PlayerOption == ComputerOption:
        return "Hòa"
    elif (PlayerOption == 1 and ComputerOption == 3) or (PlayerOption == 3 and ComputerOption == 2) or (PlayerOption == 2 and ComputerOption == 1):
        return "Người chơi"
    else:
        return "Máy"

def playBestofN(n):
    PlayerScore, ComputerScore =0, 0
    for i in range(n):
        print(f"\nRound  {i + 1} of {n}: ")
        PlayerOption = getPlayeroption()
        ComputerOption = getComputerOption()
        print(f"Computer Option is: {ComputerOption}")
        winner = determineWinner(PlayerOption, ComputerOption)

        if winner == "Người chơi":
            PlayerScore += 1
            print(f"Bạn thắng round: {i + 1}")
        elif winner == "Máy":
            ComputerScore += 1
            print(f"Máy thắng round: {i + 1}")
        else:
            print(f"Bạn và máy hòa nhau round: {i + 1} ")
        print(f"Score: Player: {PlayerScore}    ----  Computer:  {ComputerScore}")

        if (PlayerScore > n // 2) or (ComputerScore > n // 2):
            break

    if PlayerScore > ComputerScore:
        print(f"Chúc mừng bạn là người chiến thắng sau {i + 1} round!")
    elif PlayerScore < ComputerScore:
        print(f"Máy thắng , chúc bạn may mắn lần sau")
    else:
        print(f"Hòa sau {n} round")

def playDynamic():
    PlayerScore, ComputerScore, GamesPlayed = 0, 0, 0
    Option_count = {1: 0, 2: 0, 3: 0}
    while True:
        print(f"\nRound {GamesPlayed +1} ")
        PlayerOption = getPlayeroption()
        ComputerOption = getComputerOption()
        print(f"Computer's Option is:    {ComputerOption}")
        winner = determineWinner(PlayerOption, ComputerOption)
        Option_count[PlayerOption] += 1


        if winner == "Người chơi":
            PlayerScore += 1
            print("Bạn thắng round này")
        elif winner == "Máy":
            ComputerScore += 1
            print("Máy thắng round này")
        else:
            print("Bạn và máy hòa nhau round này")

        GamesPlayed += 1

        print(f"Overall"
              f"Score: PLAYER:   {PlayerScore} -----------------   COMPUTER:   {ComputerScore}")
        addRound = input("Bạn có muốn chơi thêm một Round khác không: ")
        if addRound.lower() not in["yes", "y"]:
            break

    WinProportion = (PlayerScore / GamesPlayed) * 100 if GamesPlayed > 0 else 0
    mostSelected = max(Option_count, key = Option_count.get)

    print("Overall")
    print(f"Tổng điểm người chơi:   {PlayerScore}")
    print(f"Tỷ lệ thắng:   {WinProportion}")
    if mostSelected == 1:
        return "Búa"
    elif mostSelected == 2:
        return "Bao"
    else:
        return "Kéo"
    print(f"Lựa chọn nhiều nhất: {mostSelected}")

def main():
    print("Chào mừng đến vơới trò chơi kéo búa bao!")
    while True:
        print("==============MENU==============")
        print("1. Play Best of N ROUND")
        print("2. Play Dynamic ROUND")
        print("3. Thoát")
        choice = int(input("Enter your choice(1, 2, 3): "))
        if choice == 1:
            try:
                n = int(input("Enter number of rounds: "))
                if n > 0 and n % 2 == 1:
                    playBestofN(n)
            except ValueError:
                print("Invalid input. Please enter a valid number")
        elif choice == 2:
            playDynamic()

        else:
            break
if __name__ == "__main__":
    main()

"""import random
class RockPaperScissors:
    def __init__(self):
        self.choices = {1: "Búa", 2: "Bao", 3: "Kéo"}
        self.PlayerScore = 0
        self.ComputerScore = 0
        self.GamePlayed = 0
        self.WinProportion = 0
        self.ChoiceCount = {1: 0, 2: 0, 3: 0}

    def getComputerOption(self):
        return random.choice([1, 2, 3])
    def getPlayerOption(self):
        while True:
            try:
                option = int(input("Your option is 1(Búa)  or 2(Bao)  or 3(Kéo):  "))
                if option in [1, 2, 3]:
                    return option
                print("Invalid, please enter 1 or 2 or 3")
            except ValueError:
                print("Invalid, please enter 1 or 2 or 3")
    def determineWinner(self, PlayerOption, ComputerOption):
        if PlayerOption == ComputerOption:
            return "Hòa"
        elif (
                (PlayerOption == 1 and ComputerOption == 3) or
                (PlayerOption == 2 and ComputerOption == 1) or
                (PlayerOption == 3 and ComputerOption == 2)
        ):
            return "Người chơi"
        else:
            return "Máy"


    def playBestOfN(self, n):
        self.PlayerScore = 0
        self.ComputerScore = 0
        for i in range(n):
            print(f"\nRound {i + 1} of {n}")
            player_option = self.getPlayerOption()
            computer_option = self.getComputerOption()
            print(f"Computer's option is:   {self.choices[computer_option]}")
            winner = self.determineWinner(player_option, computer_option)
            if winner == "Người chơi":
                self.PlayerScore += 1
                print(f"Bạn thắng round {i + 1}")
            elif winner == "Máy":
                print("Máy thắng round này ")
                self.ComputerScore += 1
            else:
                print(f"Bạn và máy hòa nhau round {i + 1}!")


            print(f"Score: Player:  {self.PlayerScore}------------Computer: {self.ComputerScore}" )
            if (self.PlayerScore > n // 2) or (self.ComputerScore > n // 2):
                break


        if self.PlayerScore > self.ComputerScore:
            print(f"Chúc mừng bạn là người chiến thắng sau {i + 1} Round!")
        elif self.PlayerScore < self.ComputerScore:
            print("Máy thắng chúc bạn may mắn lần sau:")
        else:
            print(f"Hòa nhau sau {n} round")

    def PlayDynamic(self):
        self.PlayerScore = 0
        self.ComputerScore = 0
        self.GamePlayed = 0
        self.OptionCout = {1: 0, 2: 0, 3: 0}
        while True:
            print(f"Round {self.GamePlayed + 1}")
            PlayerOption = self.getPlayerOption()
            ComputerOption = self.getComputerOption()
            print(f"Computer's option is: {self.choices[ComputerOption]}")
            winner = self.determineWinner(PlayerOption, ComputerOption)
            self.OptionCout[PlayerOption] += 1

            if winner == "Nguời chơi":
                print("Bạn thắng round này")
                self.PlayerScore += 1
            elif winner == "Máy":
                print("Máy thắng round này")
                self.ComputerScore += 1
            else:
                print("Bạn và máy hòa nhau round này:")

            self.GamePlayed += 1

            print(f"Overall Score: PLAYER:  {self.PlayerScore} --------------- COMPUTER:  {self.ComputerScore}")
            play_again = input("Bạn có muốn chơi thêm một round khác hay không? (yes/no):  ")
            if play_again not in ["yes", "y"]:
                break
        winProportion = (self.PlayerScore / self.GamePlayed) * 100
        mostSelected = max(self.OptionCout, key = self.OptionCout.get)
        print("Overall Result")
        print(f"Total player score: {self.PlayerScore}")
        print(f"WinProportion: {self.WinProportion:.2f}%")
        print(f"Most selected option: {self.choices[mostSelected]}")


    def main(self):
        print("Chào mừng đến với trò chơi kéo búa bao:")
        while True:
            print("=============MENU==============")
            print("1. Play Best of N ROUND")
            print("2. Play DynaMMIC ROUND")
            print("3. Thoát")
            choice = int(input("Enter your choice (1, 2, 3):  "))

            if choice == 1:
                try:
                    n = int(input("Enter number of round: "))
                    if n > 0 and n % 2 == 1:
                        self.playBestOfN(n)
                        break
                    else:
                        print("Please enter a more correct number.")
                except (ValueError, IndexError):
                    print("Please enter a valid number")

            elif choice == 2:
                self.PlayDynamic()
                break

            elif choice == 3:
                print("Thanks for your playing, see you later")
            else:
                print("Lựa chọn không hợp lệ vui lòng thử lại:")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.main()"""





















    