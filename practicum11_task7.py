all_nums = [int(num) for num in input().split()]
odd = []
even = []

for i in range(len(all_nums)):
    if all_nums[i] % 2 == 0:
        even.append(all_nums[i])
    else:
        odd.append(all_nums[i])

print(sum(even), sum(odd))




