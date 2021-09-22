import re


def get_unique_emails(filename):
    emails = set()
    with open(filename) as f:
        for line in f:
            match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
            for email in match:
                emails.add(email)

    return emails
