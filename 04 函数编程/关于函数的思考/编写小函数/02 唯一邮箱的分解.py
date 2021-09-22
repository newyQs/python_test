import re


def get_unique_emails(filename):
    ''
    emails = set()
    for line in read_file(filename):
        match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
        for email in match:
            emails.add(email)


def read_file(filename):
    '读取每一行'
    with open(filename) as f:
        for line in f:
            yield line
