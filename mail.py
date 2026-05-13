import re

def mail_extractor(file):
    with open(file, "r") as file:
        content = file.read()
        email_pattern = r'[a-z0-9._-]+@[a-z]+\.[a-z]+'
        email_extract = re.findall(email_pattern, content)
    return email_extract


print(mail_extractor("customer_records.txt"))

