"""

"""
import random
from PIL import Image


class StrUtils:
    @classmethod
    def verification_code1(cls):
        """
        获取随机验证码
        """
        s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        vc = ""
        for i in range(12):
            vc += random.choice(s)

        return vc

    @classmethod
    def verification_code2(cls):
        """
       获取随机验证码
       """
        vc = ""
        for i in range(12):
            vc += str(random.choice([
                random.randrange(10),  # 数字
                # chr(random.randrange(65, 91)),  # 大写字母
                chr(random.randrange(97, 123))  # 小写字母
            ]))

        return vc

    @classmethod
    def verification_code3(cls):
        img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))

        # 在图片查看器中打开
        # img.show()

        # 保存在本地
        with open('code.png', 'wb') as f:
            img.save(f, format='png')


su = StrUtils()

if __name__ == '__main__':
    # print(su.verification_code1())
    print(su.verification_code2())
    # su.verification_code3()
