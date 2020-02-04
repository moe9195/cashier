def main():
    name = ''
    items = []
    while True:
        item = {}
        name = input('Item (enter "done" when finished): ')
        if name == 'done':
            break;

        item['name'] = name
        item['price'] = input('Price: ')
        item['quantity'] = str(input('Quantity: '))
        items.append(item)
    sum = 0
    print('-------------')
    print('receipt')
    print('-------------')
    for item_dict in items:
        print(item_dict['quantity'] + ' ' + item_dict['name'] + ' ' + str(int(item_dict['price'])*int(item_dict['quantity']))+'KD')
        sum += (int(item_dict['price']) * int(item_dict['quantity']))
    print('-------------')
    print('Total Price: '+str(sum)+'KD')


if __name__ == '__main__':
    main()
