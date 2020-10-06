start_move = int(input("Введите кол-во километров в начале:"))
final_move = int(input("Введите кол-во километров в конце:"))
day = 1
while start_move < final_move:
    start_move = (start_move / 10) + start_move
    print(day, ":", start_move)
    day = day + 1
print("В этот день он достиг результата:", day - 1)
