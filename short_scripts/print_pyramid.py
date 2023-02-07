for i in range(5):
    pass
    # print("#"*i)

for i in range(1, 6):
    for j in range(0, i):
        print("#", end=".")

    print(end="\n")

for i in range(1, 6):
    roww = ""
    for j in range(0, i):
        roww += "#"

    print(roww)
