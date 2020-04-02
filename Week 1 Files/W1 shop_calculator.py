def main():
    items = int(input('Number of items: '))
    total_price = 0
    for i in range(1,items+1,1):
        item_price = float(input('Price of item: $'))
        total_price = total_price + item_price
    if total_price > 100:
        total_price = total_price * 0.9
    print('Total price for {} item/s is ${:.2f}'.format(items, total_price))


main()
