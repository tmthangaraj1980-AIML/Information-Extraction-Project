import re
def credit_ext(file):
    with open(file,"r") as file:
        content = file.read()
        pattern = r"\d{4}-\d{4}-\d{4}-\d{4}"
        extract = re.findall(pattern, content)
    return extract
print(credit_ext("customer_records.txt"))