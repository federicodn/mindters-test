import re

def count_emails(filename):
    with open(filename, 'r') as f:
        data = f.read()
        match = re.findall("[\w\.-]+@[\w\.-]+\.\w+", data)
        print(len(match))


count_emails('archivo_con_mails.txt')


