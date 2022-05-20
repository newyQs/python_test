import os
from django.conf import settings

file = request.FILES.get('photo')

saved_path = os.path.join(settings.MEDIA_ROOT, 'user_photos')
if not os.path.exists(saved_path):  # 如果文件路径不存在则创建文件保存目录
    os.mkdir(saved_path)

saved_file = os.path.join(saved_path, file.name)  # file.name为带后缀的文件名

with open(saved_file, 'wb+') as of:  # 以二进制留写的方式写入文件，文件不存在则自动创建
    if file.multiple_chunks():  # 判断如果文件大于默认值2.5M（可以修改）则采用分块的方式上传
        for fc in file.chunks():
            of.write(fc)
    else:
        of.write(file.read())  # 小于2.5M则直接上传
