def generate_ip():
    import random
    return '.'.join([str(random.randint(0, 255)) for _ in range(4)])
