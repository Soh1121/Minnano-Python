#!/usr/bin/env python
# coding=utf-8

from datetime import datetime

from todoitem import ToDoItem
from todocontainer import ToDoContainer

import unittest

class TestToDoContainer(unittest.TestCase):

    def setUp(self):
        """
        ToDoContainerに19個のToDoを追加する
        """
        self.todos = ToDoContainer()
        for d in range(19, 0, -1):
            td = ToDoItem('title {}'.format(d), 'desc {}'.format(d), datetime(2012, 10, d))
            self.todos += td

    def test_container(self):
        """
        ToDoContainerのToDoItem追加機能をテストする
        """
        # ToDoが19個入っているかどうか確認
        self.assertEqual(len(self.todos), 19)
        # 0番目のToDoの日付を確認
        self.assertEqual(self.todos[0].duedate.year, 2012)
        self.assertEqual(self.todos[0].duedate.day, 1)
        # 5番目のToDoの日付を確認
        self.assertEqual(self.todos[5].duedate.day, 6)
        # 5番目のToDoを消して，日付をチェック，項目が削除されているか確認
        del self.todos[5]
        self.assertEqual(self.todos[5].duedate.day, 7)

        # ToDo項目の数が減っているかどうか確認
        self.assertEqual(len(self.todos.get_remaining_todos()), 18)

    def test_remaining_todo(self):
        """
        残っているToDoを取り出す機能をテスト
        """
        # 残りのToDoが19個であることを確認
        self.assertEqual(len(self.todos.get_remaining_todos()), 19)
        # 2つのToDOを終了
        self.todos[2].finish()
        self.todos[3].finish()
        # 残りのToDoが17個であることを確認
        self.assertEqual(len(self.todos.get_remaining_todos()), 17)


if __name__ == '__main__':
    unittest.main()