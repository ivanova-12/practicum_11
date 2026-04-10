def new_str(snt:str) -> str:
    """Do a sorted list from snt
    and return a new str from this list
    """

    snt = list(snt)
    snt.sort()
    return ''.join(snt)

if __name__ == '__main__':
    print(new_str(input()))

