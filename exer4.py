value = int(input("input value"))
max_val = 0
number_move = 10
while value > 0:
    if value % number_move > max_val:
        max_val = value % number_move
    value = int(value / number_move)
print(max_val)
