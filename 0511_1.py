from tkinter import *

### 필요한 함수 정의해서 쓸 것 ###
def left():
    canvas.move(id, -3, 0)

def right():
    canvas.move(id, 3, 0)

def up():
    canvas.move(id, 0, -3)

def down():
    canvas.move(id, 0, 3)

window = Tk()

canvas = Canvas(window, bg = "white", width = 500, height = 300)
canvas.grid(row=0, column=0, columnspan=4) ## grid 에서 여러 칸을 합쳐 배치


id = canvas.create_rectangle(100, 100, 200, 200, fill = "red")

### 버튼도 알아서 만들어서 쓸 것 ###
Button(window, text = "<-(left)", command = left).grid(row=1, column=0)
Button(window, text = "(right)->", command = right).grid(row=1, column=1)
Button(window, text = "^\n|\n(up)", command = up).grid(row=1, column=2)
Button(window, text = "(down)\n|\nv", command = down).grid(row=1, column=3)

window.mainloop()
