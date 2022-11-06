# draw an f shape with nested loops

list = [5, 2, 5, 2, 2]

# own imp
for n in list:
    print(n*"*")

# tuts imp
for n in list:
    output = ''
    for i in range(n):
        output += 'X'
    print(output)
