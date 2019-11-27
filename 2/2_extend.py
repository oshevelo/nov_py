def calc_price(raw_price, vat=0.2):
    return raw_price + raw_price*vat

#print(calc_price(100, 0.2))


raw_data = [
    {'raw_price': 100},
    {'raw_price': 500, 'vat': 0}
]

for row in raw_data:
    print(calc_price(
        raw_price=row.get('raw_price', 0), vat=row.get('vat', 0.2)
    ))

for row in raw_data:
    print(calc_price(**row))






