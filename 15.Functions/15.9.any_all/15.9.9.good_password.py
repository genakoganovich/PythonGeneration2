import string


password = input()
print('YES' if len(password) >= 7
               and any(map(lambda x: x in password, string.digits))
               and any(map(lambda x: x in password, string.ascii_lowercase))
               and any(map(lambda x: x in password, string.ascii_uppercase)) else 'NO')
