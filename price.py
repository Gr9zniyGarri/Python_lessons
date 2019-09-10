def discounted(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 99:
        raise ValueError("Скидка не может быть больше 99%")
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount


product = {
    'name': 'Samsung Galaxy S10',
    'stock': 8,
    'price': 37500,
    'discount': 7.5}

product['dscounted_price'] = discounted(product['price'], product['discount'])

print(product)

discounted(50000, 17)
