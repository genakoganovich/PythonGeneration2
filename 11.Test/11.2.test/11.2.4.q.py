def build_query_string(params):
    return '&'.join([f'{key}={params[key]}' for key in sorted(params)])
