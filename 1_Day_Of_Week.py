# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

num_day = int(input('Enter number of day: '))

if num_day == 6 or num_day == 7:
    print(f'Day with number {num_day} is day off.')
elif num_day < 1 or num_day > 7:
    print(f'Day with number {num_day} is not day of the week.')
else:
    print(f'Day with number {num_day} is working day.')