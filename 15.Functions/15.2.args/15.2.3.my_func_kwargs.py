def my_func(**kwargs):
    print(type(kwargs))
    print(kwargs)


my_func()
my_func(a=1, b=2)
my_func(name='Timur', job='Teacher')
