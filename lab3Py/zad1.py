# Napisz program, który pobierze od użytkownika liczby rozdzielone przecinkiem
# a następnie policzy znajdzie ich max oraz min, bez używania wbudowanych funkcji.

numbers = input("Podaj liczby oddzielone przecinkami: ")
numbers_list = numbers.split(",")
maxvalue = numbers_list[0]
minvalue = numbers_list[0]
for x in numbers_list:
    if minvalue > x:
        minvalue = x
    if maxvalue < x:
        maxvalue = x

print(maxvalue)
print(minvalue)
