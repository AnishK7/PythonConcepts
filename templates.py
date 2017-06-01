from string import Template

class MyTemplate(Template):
    delimiter = '#'

def Main():
    cart = []
    cart.append(dict(item="Coke", price=10, qty=1))
    cart.append(dict(item="Cake", price=20, qty=2))
    cart.append(dict(item="Fish", price=30, qty=3))

    t = MyTemplate("#qty * #item = #price")
    total = 0
    print("Cart:")
    for data in cart:
        print(t.substitute(data))
        total += data['price']

    print('Total', total)

if __name__=="__main__":
    Main()
