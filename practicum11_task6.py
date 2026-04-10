num = int(input())
divisors = []

if num != 0:
    for i in range(1, abs(num)//2 + 1):
        if abs(num) % i == 0:
            divisors.append(i)

    divisors.append(num)
    if num < 0:
        for elem in divisors.copy():
            divisors.append(-elem)

print(sorted(divisors))

