d = dict()

def out_mode():
    while True:
        z = input("(검색모드) 이름을 입력하세요: ")
        if z in d:
            print("(검색모드) 전화번호는 %s 입니다." % d[z])
        elif not z:
            break
        else:
            print("(검색모드) 찾는 이름이 없습니다.")

while True:
    x = input("(입력모드) 이름을 입력하세요: ")
    if not x:
        out_mode()
        break
    elif x not in d:
        y = input("(입력모드) 전화번호를 입력하세요: ")
        d[x] = y
    else:
        print("(입력모드) 이미 등록되어 있습니다.")

