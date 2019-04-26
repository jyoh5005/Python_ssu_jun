# 초기 게임판 생성
list = [[str(i + n) for i in range(1, 4)] for n in range(0, 7, 3)]

#게임판 출력 함수
def GameBord_print():
    print("게임 상황")
    for i in range(3):
        for n in range(3):
            print(list[i][n], end=" ")
        print()

# 플레이이어 차례
def player_turn():
    print("플레이어 차례")
    while 1:
        insert_x = int(input("원하는 x좌표 입력: ")) -1
        insert_y = int(input("원하는 y좌표 입력: ")) -1
        if list[insert_x][insert_y] in ["@", "X"]:
            print("재입력해 주시기 바랍니다.")
        else:
            list[insert_x][insert_y] = "@"
            break

# 컴퓨터 차례
def computer_turn():
    print("컴퓨터 차례")
    for i in range(3):
        for n in range(3):
            if list[i][n] not in ["@", "X"]:
                list[i][n] = "X"
                return

# 게임
print("게임을 시작합니다.")
GameBord_print()
player_turn()
GameBord_print()
for z in range(4):
    computer_turn()
    GameBord_print()
    player_turn()
    GameBord_print()
