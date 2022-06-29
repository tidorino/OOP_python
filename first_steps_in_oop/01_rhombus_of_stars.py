def get_line(i, n):
    space_count = n - 1 - i
    stars = i + 1
    return ' ' * space_count + '* ' * stars


def rhombus_of_stars(n):
    [print(get_line(i, n)) for i in range(n)]

    for i in range(n - 2, -1, -1):
        print(get_line(i, n))


n = int(input())

rhombus_of_stars(n)
