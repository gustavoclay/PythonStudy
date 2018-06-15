import urllib.request
import time
def view_price():
    page = urllib.request.urlopen('http://beans.itcarlow.ie/prices-loyalty.html')
    text = page.read().decode('utf-8')
    where = text.find('>$')
    start = where + 2
    end = start + 4
    return float(text[start:end])


option = input('Deseja comprar já? (S/N): ')
if option == 'S':
    price = view_price()
    print('Comprar! Preço: %5.2f' % price)
else:
    price = 99.9
    while price >= 4.74:
        price = view_price()
        if price >= 4.74:
            time.sleep(600)
    print('Comprar! Preço: %5.2f' % price)
