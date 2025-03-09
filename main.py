def print_hi(name):
    print(f'Hi, {name}')


def sort_list(lst):
    lst.sort()
    return lst


def main():
    lastname = input("Enter Your lastname: ")
    lastname = lastname.lower()
    print_hi(lastname)

    lst = [123, 1.2, 34, 67, 1, 98, 134, 23, 54]
    print(sort_list(lst))


main()
