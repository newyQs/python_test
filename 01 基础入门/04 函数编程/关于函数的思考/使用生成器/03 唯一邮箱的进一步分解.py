import re


def get_unqiue_emails(filename):
    for line in read_file(filename):
        match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
        for email in match:
            yield email


def read_file(filename):
    with open(filename) as f:
        for line in f:
            yield line


def print_email_list():
    for email in get_unqiue_emails('duplicate_emails'):
        print(email)

'''
生成器的使用可以使你的代码更加简洁，并且可以规避内存占用的问题。
'''