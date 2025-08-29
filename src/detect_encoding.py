import chardet

with open("data/ecommerce_sales.csv", "rb") as f:
    result = chardet.detect(f.read())
    print(result)
