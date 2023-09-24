import re
text = '''Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!'''

w = 'world'
text = re.sub(w, '*' * len(w), text)
print(text)

