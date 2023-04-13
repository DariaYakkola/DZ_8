width = int(input('Введите горизонтальное количество долек: '))
lenght = int(input('Введите вертикальное количество долек: '))
piece = int(input('Какой кусочек хотим отломить? '))
if (piece % lenght == 0 or piece % width == 0) and (piece < width * lenght):
    print('Мы можем отломить этот кусочек! ')
else:
    print('Мы не можем отломить такой кусочек!')
