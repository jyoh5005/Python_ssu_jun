from tkinter import *

wd = Tk()
country = ['미국', '영국', '프랑스', '일본']
button_list = []

def number_plus(x):
    button = button_list[x][0]
    button_list[x][1] += 1
    button["text"] = country[x]+": "+str((button_list[x][1]))

for x in range(4):
    b = Button(wd, text=(country[x]+": 0"), command=lambda i = x: number_plus(i))
    b.grid(row=x)
    button_list.append([b, 0])

wd.mainloop()
