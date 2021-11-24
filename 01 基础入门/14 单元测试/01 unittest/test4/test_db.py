import unittest
from db import app, db, Author, Book
import time


class TestLogin(unittest.TestCase):
    """定义测试案例"""

    def setUp(self):
        """在执行具体的测试方法前，先被调用"""

        # 激活测试标志
        app.config['TESTING'] = True

        # 设置用来测试的数据库，避免使用正式数据库实例[覆盖原来项目中的数据库配置]
        user = 'root'
        password = '***********'
        # 设置数据库，测试之前需要创建好 create database testdb charset=utf8;
        database = 'testdb'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@127.0.0.1:3306/%s' % (user, password, database)

        self.app = app

        # 创建数据库的所有模型表：Author、Book模型表
        db.create_all()

    def tearDown(self):
        # 测试结束操作，删除数据库
        db.session.remove()
        db.drop_all()

    # 测试代码
    def test_append_data(self):
        au = Author(name='quyuan')
        bk = Book(info='python_book')
        db.session.add_all([au, bk])
        db.session.commit()
        author = Author.query.filter_by(name='quyuan').first()
        book = Book.query.filter_by(info='python_book').first()
        # 断言数据存在
        self.assertIsNotNone(author)
        self.assertIsNotNone(book)

        # 休眠10秒，可以到数据库中查询表进行确认
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
