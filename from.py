#! /usr/bin/env python
import tkinter

# ↓ボタンクリック時に実行される関数
def Calculation_1():
    val_1 = int(num_area.get())
    answer = (val_1 **2)
    answer_ent.delete(0, tkinter.END)
    answer_ent.insert(0, answer)

# ↓ベースとなるGUIの作成
root = tkinter.Tk()

# ↓GUIのタイトル
root.title(u'統計学簡略化ツール')
# ↓GUIのサイズ
root.geometry('320x100')

# GUI上に入力部分を表示させるラベル
sd_label_1 = tkinter.Label(root, text='分散')
sd_label_1.place(x=60, y=10)

# GUI状に答えを表示させるラベル
v_label = tkinter.Label(root, text='標準偏差')
v_label.place(x=180, y=10)

# ↓GUI上に矢印を表示するラベル
plus_label = tkinter.Label(master=root, text='→', font=20)
plus_label.place(x=135, y=25)

# ↓テキストエリア作成,計算問題を入力する
num_area = tkinter.Entry(master=root, width=5, font=20)
num_area.place(x=60, y=30)

# ↓ボタン作成,クリックで計算処理を実行する
answer_btn = tkinter.Button(master=root, text='Answer', command=Calculation_1)
answer_btn.place(x=240, y=30)

# ↓計算結果が表示されるラベル
answer_ent = tkinter.Entry(master=root, width=5, font=20)
answer_ent.place(x=180, y=30)

root.mainloop()