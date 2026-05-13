import re

def phone_extractor(file):
    with open (file,"r") as file:
        content = file.read()
        pattern = r"\d{4}\s\d{4}\s\d{4}"
        extract = re.findall(pattern, content)
    return extract

print(phone_extractor("customer_records.txt"))