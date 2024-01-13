#выводим поле
field = [
    ['.' for _ in range(3)] #массив из точек 3 на 3
    for _ in range(3)
]

def print_field():
    for row in field:
        for cell in row:
            print(cell, end=' ')
        print()
print_field()

def player_move():
    print('Please enter your move (row,col): ')
    move = input()
    row, col = move.split(',')
    row, col = int(row) - 1, int(col) - 1

    if field[row][col] != '.':
        print('Cell is already taken')
    else:
        field[row][col] = 'X'
# ход компьютера
from random import randint

def ai_move():
    x = randint(0, 2)
    y = randint(0, 2)
    while field[x][y] != '.':
        x = randint(0, 2)
        y = randint(0, 2)
    field[x][y] = 'O'

WINS = [
    [(0,0), (0,1), (0,2)], # 0-я строка
    [(1,0), (1,1), (1,2)], # 1-я строка
    [(2,0), (2,1), (2,2  )], # 2-я строка
    [(0,0), (1,0), (2,0)], # 0-й столбец
    [(0,1), (1,1), (2,1)], # 1-й столбец
    [(0,2), (1,2), (2,2)], # 2-й столбец
    [(0,0), (1,1), (2,2)], # главная диагональ
    [(0,2), (1,1), (2,0)]  # побочная диагональ
]

def check_win():
    for option in WINS:
        # print(f'Checking option {option}:')
        values = []
        for cell in option:
            row, col = cell
            value = field[row][col]
            # print(f'\t-cell {cell} has value {value}')
            values.append(value)
        if values[0] == values[1] == values[2] != '.':
            # print(f'All values are equal to {values[0]}, returning!')
            return values[0]

check_win()

while True:
    player_move()
    print_field()
    if check_win() == 'X':
        print('You won!')
        break
    ai_move()
    print_field()
    if check_win() == 'O':
        print('Computer wins!')
        break