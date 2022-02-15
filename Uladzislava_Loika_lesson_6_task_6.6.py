import sys

with open('bakery.csv', 'a+', encoding='utf-8') as f:
    code, price = sys.argv
    amount_int = float(price.replace(',', '.'))
    f.write(f'{amount_int}' + '\n')

