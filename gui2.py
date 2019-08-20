from tkinter import *
import tkinter.messagebox as mb
import tkinter as tk
count = 0
sta= mb.showinfo("問題！","どっちが正解？")
que1 = mb.askyesno("問題１", "警視庁には、７００万分以上の指紋が登録されているが指紋の持ち主が５５歳になったとき削除される？")
if que1 == False:
    count += 1
que2 = mb.askyesno("問題２","マムシに噛まれると即死する？")
if que2 == False:
    count += 1
que3 = mb.askyesno("問題３","狂犬病に感染し、発症すると１００％助からない")
if que3 == True:
    count += 1


#s = ["１）No:登録抹消は７５歳で行われる。犯罪率が極端に下がるため。", "２）No:マムシに噛まれて死亡する確率は０．５以下。", "３）yes:違うのは着色料と香料で、それにより脳が錯覚を起こし、それぞれの味を認識してしまうため。{}"]
def yes_no():
    mb.showinfo("解答", "１）No:登録抹消は７５歳で行われる。犯罪率が極端に下がるため。, ２）No:マムシに噛まれて死亡する確率は０．５以下。, ３）yes:違うのは着色料と香料で、それにより脳が錯覚を起こし、それぞれの味を認識してしまうため。  {}問正解".format(count))


root = Tk()
root.title("解答！")
root.geometry('200x150')

YesNo_button = Button(root,
    text="解答",
    width=10, height=3,
    command=yes_no
)
YesNo_button.pack()


root.mainloop()
