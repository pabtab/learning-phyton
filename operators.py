is_hot = False
is_cold = False

if is_hot:
    print('Its hot day')
elif is_cold:
    print('Its cold day')
else:
    print('lovely day')
print('Enjoy the day')


buyer_good_credit = False
put_down = 0
price = 1000000
whatever = True
something = False

if buyer_good_credit and whatever or not something:
    print('10% less')
    put_down = 10
else:
    print('20% less')
    put_down = 20

down_price = price * (put_down / 100)
print(down_price)
print(f"Your price is: {price - down_price}")
