def is_triangle(a, b, c):
    lines = [a,b,c]
    max1 = max(lines)
    lines.remove(max1)
    if ((lines[0] + lines[1]) > (max1)):
        return True
        print("works when sides were {}, {}, {}".format (a,b,c))
    else:
        return False
        print("didn't work when sides were {}, {}, {}".format (a,b,c))
