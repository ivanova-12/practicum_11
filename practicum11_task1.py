list_of_start = []
list_of_end = []

for i in range(10):
    num = int(input())
    list_of_start.append(num)

for i in range(1, len(list_of_start) - 1):
    list_of_end.append(list_of_start[i-1] + list_of_start[i+1])

print(list_of_end)
