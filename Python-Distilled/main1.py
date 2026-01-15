a = 7
b = 6
c = a if a > b else b
print(c)

d = 0
while (d := d + 1) < 10:
    print("d: ", d)

print('''Content-type: text/html
<h1> Hello World </h1>
Click <a href="http://www.python.org">here</a>.
''')

base_year = 100000000
year = 2
principal = 0.12342345
print(f'{base_year + year:>4d}')
print(f'principal: {principal:0.2}')
print('principal: {0:0.3f}' .format(principal))

print("repr: ", repr(principal))
