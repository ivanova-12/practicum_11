lst = [int(num) for num in input().split()]
operation = input()
real_operation = int(operation[1:])


if len(lst) < real_operation:
    if len(lst) != 0:
        real_operation = real_operation % len(lst)

if operation[0] == 'R':
    print(lst[-real_operation:] + lst[:-real_operation])
else:
    print(lst[real_operation:] + lst[:real_operation])

