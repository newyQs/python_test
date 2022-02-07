import unittest
import demo


class DateServiceTest(unittest.TestCase):
    """
    test clean_tb_async_src_acct.py
    """

    def setup(self):
        """在这里做资源的初始化 """
        pass

    def tearDown(self):
        """在这里做资源的释放 """
        pass

    def test_get_date_year_month_1(self):
        """ 测试方法1，测试方法应该以test_开头 """

        pm_date = "2015-11-25 14:40:52"
        year, month = demo.get_date_year_month(pm_date)
        self.assertEqual(year, "2015", "year not equal")
        self.assertEqual(month, "11", "month not equal")

    def test_get_date_year_month_2(self):
        """ 测试方法1，测试方法应该以test_开头 """

        pm_date = "20161225144052"
        year, month = demo.get_date_year_month(pm_date)
        self.assertEqual(year, "2016", "year not equal")
        self.assertEqual(month, "12", "month not equal")


# test 文件及目录操作
if __name__ == "__main__":
    unittest.main()
