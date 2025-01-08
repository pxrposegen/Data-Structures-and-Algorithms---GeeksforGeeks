class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def do_overlap(l1, r1, l2, r2):
    if l1.x > r2.x or l2.x > r1.x:
        return False

    if r1.y > l2.y or r2.y > l1.y:
        return False

    return True


l1 = Point(0, 10)
r1 = Point(10, 0)
l2 = Point(5, 5)
r2 = Point(15, 0)

if do_overlap(l1, r1, l2, r2):
    print("Rectangles Overlap")
else:
    print("Rectangles Don't Overlap")