def add_three(input_var):
    return input_var + 3


# print(add_three(3))

def get_pay(hours):
    pay = hours * 15
    return pay * (1 - .12)


print(get_pay(200))
