def new_lsts() -> None:
    """change the start lists with help of a part first:
    delete it from the 1st list
    extend reverse version to 2nd list
    """

    lst1 = [int(num) for num in input().split()]
    lst2 = [int(num) for num in input().split()]
    start, end = map(int, input().split())

    plus_lst = lst1[start:end + 1]
    lst1 = lst1[:start] + lst1[end + 1:]
    plus_lst.reverse()
    lst2.extend(plus_lst)

    print(lst1, lst2)


if __name__ == '__main__':
    new_lsts()

