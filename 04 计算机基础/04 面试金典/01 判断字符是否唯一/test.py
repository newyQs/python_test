"""

"""


def is_unique_str(ss: str) -> bool:
    for i in ss:
        for j in ss:
            return i != j


if __name__ == '__main__':
    print(is_unique_str('leetcode'))
