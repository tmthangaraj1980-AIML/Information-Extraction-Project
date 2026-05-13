import re

with open("customer_records.txt","r") as file:
    content = file.read()
    pattern = r"[6-9]\d{4}\s\d{5}"
    extract = re.findall(pattern, content)
    print(extract)