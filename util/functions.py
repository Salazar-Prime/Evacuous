import math

def slope(a, b):
    """Slope of vector from position vector `a` to `b`"""
    ax, ay = a
    bx, by = b
    try:
        return 1.0*(by-ay)/(bx-ax)
    except ZeroDivisionError:
        raise ZeroDivisionError("Slope infinite for ({},{}) - ({},{})".format(ax, ay, bx, by))

def slope_(x1, y1, x2, y2):
    """Slope vector of a line from point (x1, y1) to (x2, y2)"""
    return slope((x1, y1), (x2, y2))

def perp(a):
    """Unit vector perpendicular to given vector `a`(rotated 90deg counterclockwise)"""
    ax, ay = a
    m = magnitude(a)
    return (-ay/m, ax/m)

def magnitude(a):
    """Magnitude of a vector `a` """
    return math.sqrt(a[0]**2 + a[1]**2)

def dot(a, b):
    """Dot product of 2-d vectors `a` and `b`"""
    return a[0]*b[0] + a[1]*b[1]

def add(a, b):
    """Sum of 2-d vectors `a` and `b`"""
    return a[0]+b[0], a[1]+b[1]

def sub(a, b):
    """Difference of 2-d vectors `a` and `b`"""
    return a[0]-b[0], a[1]-b[1]

def weight_add(a, b, aw, bw):
    """Weighted addition of 2-vectors `a` and `b` as per weights *aw* and `bw`"""
    return aw*a[0]+bw*b[0], aw*a[1]+bw*b[1]

def scale(a, k):
    """Scale a 2-d vector `a` by factor `k`"""
    return k*a[0], k*a[1]

def projection(a, b):
    """Projection of vector `a` on `b`"""
    return scale(b, dot(a, b)/magnitude(b)**2)

def calc_y_on_circle(a,b,x,separation):
    """Calculates the y co-ordinate given x for circle (x-a)^2 + (y-b)^2 = (separation)^2"""
    return math.sqrt((separation)**2 - (x-a)**2) + b,-math.sqrt((separation)**2 - (x-a)**2) + b

def dist(a, b):
    """Calculate the euclidian distance between two points"""
    return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))