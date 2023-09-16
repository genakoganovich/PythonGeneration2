def print_products(*args):
    products = list(filter(lambda x: type(x) is str and x, args))
    if not products:
        print('Нет продуктов')
    else:
        for count, prod in enumerate(products, start=1):
            print(f'{count}) {prod}')


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')
