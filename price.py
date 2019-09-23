def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError("Скидка не может быть больше 99%")
        elif discount > max_discount:
            return price
        else:   
            return price - (price * discount / 100)
    except(ValueError):
        print("Неправильное значение")



product = {'name': 'Samsung Galaxy S10',
           'stock': 8,
           'price': 37500,
           'discount': 7.5}

product['dscounted_price'] = discounted(product['price'], product['discount'])

print(product)

print(discounted('', 12))


def format_price(price: int):
    return f'Цена: {price} руб.'

print(format_price(58.76))
