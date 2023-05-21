def rectangle_check(x1, y1, x2, y2, x, y):
    bigger_x = x1
    smaller_x = x2
    if x1 < x2:
        bigger_x = x2
        smaller_x = x1

    bigger_y = y1
    smaller_y = y2
    if y1 < y2:
        bigger_y = y2
        smaller_y = y1

    if smaller_x <= x <= bigger_x and (smaller_y == y or bigger_y == y):
        print("Border")
        exit()

    if (smaller_x == x or bigger_x == x) and smaller_y <= y <= bigger_y:
        print("Border")
        exit()

    print("Inside / Outside")


n_1 = float(input())
n_2 = float(input())
n_3 = float(input())
n_4 = float(input())
n_5 = float(input())
n_6 = float(input())

rectangle_check(n_1, n_2, n_3, n_4, n_5, n_6)

