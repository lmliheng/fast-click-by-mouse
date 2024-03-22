import time
from pynput.mouse import Button as Bu
from pynput.mouse import Controller as Ctrl1
from time import sleep
from tkinter.messagebox import showinfo
from ttkbootstrap import Combobox
from tkinter import Tk, Label, Entry, Button
from keyboard import wait

mouse = Ctrl1()


def start():
    showinfo("提示", "准备连点,按下w键开始。")
    wait('w')
    start_time = time.time()
    if cli.get() == "左键连点":
        for i in range(int(entry1.get())):
            mouse.click(Bu.left)
            sleep(float(entry.get()))
    elif cli.get() == "左键双击连点":
        for i in range(int(entry1.get())):
            mouse.click(Bu.left, 2)
            sleep(float(entry.get()))
    elif cli.get() == "右键连点":
        for i in range(int(entry1.get())):
            mouse.click(Bu.right)
            sleep(float(entry.get()))
    elif cli.get() == "右键双击连点":
        for i in range(int(entry1.get())):
            mouse.click(Bu.right, 2)
            sleep(float(entry.get()))
    end_time = time.time()
    elapsed_time = end_time - start_time

    # 计算预计点击时间
    total_click_time = float(entry.get()) * int(entry1.get())
    total_click_time_minutes = total_click_time / 60

    # 显示预计点击时间
    Label(app, text=f"预计点击时间：{total_click_time_minutes:.2f}分钟").place(x=90, y=110)

    showinfo("提示", f"连点结束。耗时：{elapsed_time:.2f}秒。")


if __name__ == "__main__":
    app = Tk()
    app.title("连点器")
    app.geometry('300x200')

    label = Label(app, text='''连点按键:''')
    label.place(x=8, y=20)
    label1 = Label(app, text='''连点总数:''')
    label1.place(x=8, y=50)
    label1 = Label(app, text='''时间间隔(秒):''')
    label1.place(x=8, y=80)
    cli = Combobox(app)  # 初始化
    cli["values"] = ("左键连点", "左键双击连点", "右键连点", "右键双击连点")
    cli.current(0)
    cli.configure(state='readonly')
    cli.place(x=90, y=10)

    entry1 = Entry(app, width=23)
    entry1.place(x=90, y=50)
    entry = Entry(app, width=23)
    entry.place(x=90, y=80)

    button = Button(app, text='开始连点', command=start)
    button.place(x=130, y=150)
    app.mainloop()