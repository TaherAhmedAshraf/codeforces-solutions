weights = input('').split()
a = int(weights[0])
b = int(weights[1])
years = 0

while a <= b:
    a *= 3
    b *= 2
    years += 1

print(years)