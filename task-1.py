def converter(symbol, reverse=False) -> int:
    if symbol == 'I':
        return -1 if reverse else 1
    if symbol == 'V':
        return -5 if reverse else 5
    if symbol == 'X':
        return -10 if reverse else 10
    if symbol == 'L':
        return -50 if reverse else 50
    if symbol == 'C':
        return -100 if reverse else 100
    if symbol == 'D':
        return -500 if reverse else 500
    if symbol == 'M':
        return -1000 if reverse else 1000


symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

number = input('Enter a combination: ')
count = len(number)
result = 0

if count < 2:
    result = converter(number)
else:
    prev = number[0]
    for item in number[1:]:
        if symbols.index(prev) < symbols.index(item):
            result += converter(prev, reverse=True)
        else:
            result += converter(prev)
        prev = item
    result += converter(prev)

print(result)
