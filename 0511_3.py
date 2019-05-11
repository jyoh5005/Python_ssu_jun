from tkinter import *
d = dict()
def store():
    global e_name, e_job, e_country
    name = e_name.get()
    job = e_job.get()
    country = e_country.get()
    if not name or not job or not country:
        store_button["text"] = "제대로 입력해 주세요"
    else:
       d[name] = [job, country]
       store_button["text"] = "저장할 데이터를 입력하새요"

    e_name.delete(0, END)
    e_job.delete(0, END)
    e_country.delete(0, END)

def search():
    name = e_name.get()
    if name in d:
        print(name+"의 정보: ", d.get(name))
    else:
        print("이름이 존재하지 않습니다.")

    e_name.delete(0, END)

wd = Tk()
Label(wd, text="이름"). grid(row=0)
Label(wd, text="직업"). grid(row=1)
Label(wd, text="국적"). grid(row=2)

e_name = Entry(wd)
e_name.grid(row=0, column=1)
e_job =  Entry(wd)
e_job.grid(row=1, column=1)
e_country = Entry(wd)
e_country.grid(row=2, column=1)


Button(wd, text="저장", command=store).grid(row=3)
Button(wd, text="검색", command=search).grid(row=4)

store_button = Label(wd, text="저장할 데이터를 입력하새요")
store_button.grid(row=3, column=1)
search_button = Label(wd, text="검색할 이름을 입력하세요")
search_button.grid(row=4, column=1)

wd.mainloop()
