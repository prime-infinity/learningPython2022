# a list is just like an array in javascript or golang
names = ["osamede", "prime", "agen", "elon", "musk"]

print(names[3])
print(names[-1])  # last element of list,very useful
names[-1] = "dusk"  # change element in list
print(names[-1])
print(len(names))  # length of list, not index length, take note
print(names[0:3])  # select range, from first, to last, but not including last

for i in names:
    print(i)
