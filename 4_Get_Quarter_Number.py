# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
coor_num = int(input('Enter a quarter number: '))

if   coor_num == 1: print('This quarter has coordinates: x from 0 to infinity and y from 0 to infiniti') 
elif coor_num == 2: print('This quarter has coordinates: x from 0 to negative infinity and y from 0 to infiniti')  
elif coor_num == 3: print('This quarter has coordinates: x from 0 to negative infinity and y from 0 to negative infiniti')
elif coor_num == 4: print('This quarter has coordinates: x from 0 to infinity and y from 0 to negative infiniti')
else:        print('The quarter with this number is not exist!!!')