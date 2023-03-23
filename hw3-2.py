N = abs(int(input('Enter count of elements A: ')))
A_entered = input("Enter list elements separated by a space: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N or N == 0:
    print('No match!')
else:
    X = int(input('Enter X, to compare the elements of the list: '))
    min = abs(X - A_num[0])
    index = 0
    for i in range(1, N):
        count = abs(X - A_num[i])
        if count < min:
            min = count
            index = i
    print(f'Number {A_num[index]} in list A is closest in value to the number {X}, their difference is {abs(X - A_num[index])}')