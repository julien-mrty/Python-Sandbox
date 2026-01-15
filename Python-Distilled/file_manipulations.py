with open("example.txt") as file:
    for line in file:
        print(line, end='') # Omits the EOF statement
print()

with open("example.txt") as file:
    data = file.read()

print(data)

# To read large files in chunk
with open("example.txt") as file:
    while chunk := file.read(1):
        print(chunk, end='')

num = 1
with open("out.txt", "wt") as out:
    while num < 10:
        out.write(f'{num:0.4f}\n')
        num *= 1.2