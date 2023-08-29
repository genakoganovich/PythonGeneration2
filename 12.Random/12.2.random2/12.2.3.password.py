import string
import re


symbols_to_remove = 'lI1oO0'
symbols = re.sub(rf'[{symbols_to_remove}]', '', string.ascii_letters + string.digits)

n = int(input())
m = int(input())
