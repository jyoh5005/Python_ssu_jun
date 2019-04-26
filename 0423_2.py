number_keypad = {"ABC":2, "DEF":3, "GHI":4, "JKL":5, "MNO":6, "PQRS":7, "TUV":8, "WXYZ":9}
string = input("문자열 입력: ")
for x in string:
    for item in number_keypad:
        if x in item:
            print(number_keypad[item])
