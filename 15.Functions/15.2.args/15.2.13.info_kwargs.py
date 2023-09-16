def info_kwargs(**kwargs):
    sorted_dict = dict(sorted(kwargs.items()))
    list(map(lambda k: print(f'{k}: {sorted_dict[k]}'), sorted_dict.keys()))


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
