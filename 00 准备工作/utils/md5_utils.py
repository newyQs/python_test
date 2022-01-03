"""
md5(), sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s(),
sha3_224, sha3_256, sha3_384, sha3_512, shake_128, and shake_256.

Hash objects have these methods:
update(data)
digest()
hexdigest()
copy()
"""
import os
import hashlib


class Md5Utils:

    @classmethod
    def get_file_md5(cls, file_path):
        """
        获取文件的md5
        """
        if os.path.isfile(file_path):
            hash_md5 = hashlib.md5()
            with open(file_path, "rb") as f:
                data = f.read(4096)
                while True:
                    if not data:
                        break
                    hash_md5.update(data)

            return hash_md5.hexdigest()

        else:
            print(f"文件【{file_path}】不存在.")


mu = Md5Utils()
if __name__ == '__main__':
    mu.get_file_md5()
