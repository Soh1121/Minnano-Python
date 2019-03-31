#!/Users/soichi/.pyenv/shims/python

# 標準ライブラリをインポート
from datetime import datetime
from pickle import dump, load

# GUIライブラリをインポート
from tkinter import *
import tkinter.messagebox

# データ用のクラスをインポート
from todoitem import ToDoItem
from todocontainer import ToDoContainer

# データ保存用ファイル名
DUMPFILE = 'todo.dat'

class ToDoApp(Frame):
    """
    ToDo GUIアプリ用のクラス
    """

    def createwidgets(self):
        """
        ボタンなどウィンドウの部品を作る
        """
        # スクロールバー付きリストボックス
        self.frame1 = Frame(self)
        frame = self.frame1

        self.listbox = Listbox(frame, height = 10, width = 30, selectmode = SINGLE, takefocus = 1)
        self.yscrool = Scrollbar(frame, orient = VERTICAL)

        # 配置を決める
        self.listbox.grid(row = 0, column = 0, sticky = NS)
        self.yscroll.grid(row = 0, column = 1, sticky = NS)

        # 動きとコードをつなげる
        self.yscroll.config(command = self.listbox.yview)
        self.listbox.config(yscrollcommand = self.yscroll.set)
        self.listbox.bind("<ButtonRelease-1>", self.selsectitem)

        self.frame1.grid(row = 0, column = 0)