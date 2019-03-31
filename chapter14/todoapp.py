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

    def setlistitems(self):
        """
        ToDoのうち未消化分をリストに表示する
        """
        self.listbox.delete(0, END)
        for todo in self.todos.get_remaining_todos():
            d = todo.duedate
            t = todo.title.ljust(20)
            if todo.duedate < datetime.now():
                t = '* ' + t    # ToDoの期限が過ぎていたら*を前につける
            item = "{} {:4}/{:02}/{:02} {:02}:
            {:02}".format(t, d.year, d.month, d.day, d.hour, d.minute)
            self.listbox.insert(END, item)
    
    def refrectententries(self, todo):
        """
        フィールドに入力された文字列をToDoItemインスタンスに反映する
        """
        todo.title = self.title_e.get()
        todo.description = self.description_e.get()
        dt = datetime.strptime(self.duedate_e.get() + ':00', '%Y/%m/%d %H:%M:%S')
        todo.duedate = dt
        if self.finished_v.get() != 0:
            todo.finish()
    
    def createitem(self):
        """
        新しいToDoアイテムを作る
        """
        todo = ToDoItem('', '', datetime.now())
        self.refrectententries(todo)
        self.todos += todo
        self.clearentries()
        self.setlistitems()
        self.sel_index = -1
        self.save()

    def refreshitems(self):
        """
        タイマーで定期的に呼び出されるメソッド
        ToDoのうち時間になったものがあればダイアログで知らせる
        """
        dirty = False
        for todo in self.todos.get_remaining_todos():
            td = datetime.now()
            d = todo.duedate
            if (d.year == td.year == td.year and d.month == td.month and d.day == td.day and d.hour == td.hour and d.minute == td.minute):
                msg = "{}の時間です。\n {}\n {}".format(
                        todo.title,
                        todo.description,
                        todo.duedate.strftime('%Y/%m/%d %H:%M')
                    )
                tkinter.messagebox.showwarning("時間です", msg)
                dirty = True
        sec = datetime.now().second
        self.after((60 - sec) * 1000, self.refreshitems)

        if dirty:
            self.setlistitems()
