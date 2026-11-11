"""Exact decision procedure for relation (7) of the variable-shift bridge.

This specifies a decidable relation on FIVE ORDINARY INTEGERS. It is not
a rational Diophantine definition or a DPRM compiler. Python integers
and Fractions implement the corresponding unbounded exact arithmetic;
physical resource limits are not mathematical rejection conditions.

The height constant is exactly H6(S0), S0 = primes at most 324.
No floating-point approximation, timeout, or bounded witness search is
part of the decision procedure.
"""

from fractions import Fraction as Q


CONTACTS = (0, -15, -20, -24, -30, -60)
ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))
CURVE_A = (Q(-11243), Q(7950))
POINT_P = ((Q(1641, 8), Q(-1160, 8)),
           (Q(-123720, 32), Q(87483, 32)))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[0], -a[1])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    return (a[0] * b[0] + 2 * a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def scale(a, n):
    return (n * a[0], n * a[1])


def inverse(a):
    norm = a[0] * a[0] - 2 * a[1] * a[1]
    if not norm:
        raise ZeroDivisionError("zero element of Q(sqrt(2))")
    return (a[0] / norm, -a[1] / norm)


def divide(a, b):
    return mul(a, inverse(b))


def on_curve(point):
    if point is None:
        return True
    x, y = point
    return mul(y, y) == add(mul(mul(x, x), x), mul(CURVE_A, x))


def point_add(left, right):
    if left is None:
        return right
    if right is None:
        return left
    x1, y1 = left
    x2, y2 = right
    if x1 == x2 and y1 == neg(y2):
        return None
    if x1 == x2:
        if y1 != y2:
            raise ValueError("inputs are not points on the specified curve")
        slope = divide(add(scale(mul(x1, x1), 3), CURVE_A), scale(y1, 2))
    else:
        slope = divide(sub(y2, y1), sub(x2, x1))
    x3 = sub(sub(mul(slope, slope), x1), x2)
    return (x3, sub(mul(slope, sub(x1, x3)), y1))


def point_multiple(n):
    base = POINT_P
    if n < 0:
        base = (base[0], neg(base[1]))
        n = -n
    result = None
    while n:
        if n & 1:
            result = point_add(result, base)
        n >>= 1
        if n:
            base = point_add(base, base)
    return result


def z(point):
    if point is None:
        return ZERO
    x, y = point
    return divide(neg(x), y)


def epsilon(index):
    u, v = z(point_multiple(index))
    return abs(u) + abs(v)


def center(a, j):
    # Tr(u+v*sqrt(2))/2 = u.
    return divide(z(point_multiple(j)), z(point_multiple(a)))[0]


class Capped:
    """Exact nonnegative arithmetic, with cap+1 denoting every larger value."""

    def __init__(self, cap):
        if cap < 1:
            raise ValueError("cap must be positive")
        self.cap = cap
        self.over = cap + 1

    def value(self, n):
        if n < 0:
            raise ValueError("capped arithmetic is nonnegative")
        return min(n, self.over)

    def add(self, *values):
        return self.value(sum(values))

    def mul(self, a, b):
        if a == 0 or b == 0:
            return 0
        if a > self.cap // b:
            return self.over
        return a * b

    def power(self, base, exponent):
        if base < 0 or exponent < 0:
            raise ValueError("nonnegative base and exponent required")
        if exponent == 0:
            return 1
        if base <= 1:
            return base
        result = 1
        while exponent:
            if base > self.cap:
                return self.over
            if exponent & 1:
                result = self.mul(result, base)
                if result == self.over:
                    return result
            exponent >>= 1
            if exponent:
                base = self.mul(base, base)
        return result

    def factorial(self, n):
        result = 1
        for factor in range(2, n + 1):
            result = self.mul(result, factor)
            if result == self.over:
                break
        return result


def height_constant_capped(cap):
    """Return min(H6(primes <= 324), cap+1), without expanding H6."""
    if cap < 0:
        raise ValueError("cap must be nonnegative")
    if cap == 0:
        return 1
    c = Capped(cap)
    d0 = c.factorial(324)
    d = c.mul(d0, c.power(3, c.mul(256, c.power(d0, 4))))
    g0 = c.value(116064000000)
    e0 = c.mul(10, c.power(c.mul(d, g0), 2))
    # The largest prime at most 324 is 317.
    r = max(d, c.value(317), c.value(10 ** 12))
    q0 = c.power(r, c.mul(r, e0))
    d_squared = c.power(d, 2)
    b_cm = c.add(c.mul(d_squared, c.power(3, c.mul(21000, d_squared))), 1)
    c_cm = c.add(c.mul(2, b_cm),
                 c.mul(4096, c.add(1028, c.mul(5, d),
                                   c.mul(84000, d_squared))))
    return c.mul(2 * 10 ** 13, max(1, c_cm, c.power(q0, 17)))


def contact_product(n):
    product = 1
    for contact in CONTACTS:
        product *= n - contact
    return product


def maximum_precision_exponent(eps):
    """Largest integer B >= 0 with 4*eps < 4**(-B), or -1 if none."""
    if eps <= 0:
        raise ValueError("epsilon must be positive")
    limit = (eps.denominator - 1) // (4 * eps.numerator)
    if limit < 1:
        return -1
    return (limit.bit_length() - 1) // 2


def precision_is_sufficient(n, kappa, eps):
    bound = maximum_precision_exponent(eps)
    if bound < 1:
        # H6 and |kappa*F(n)| are positive on the guarded input domain.
        return False
    c = Capped(bound)
    required = c.mul(height_constant_capped(bound),
                     c.power(abs(kappa * contact_product(n)), 24))
    return required <= bound


def accepts(n, kappa, a, ell, j):
    """Decide the fixed five-integer precision relation of the bridge."""
    if any(type(value) is not int for value in (n, kappa, a, ell, j)):
        raise TypeError("five ordinary integers required")
    if n in CONTACTS or kappa == 0 or a < 1 or ell < 1 or j != n * a:
        return False
    try:
        eps = epsilon(ell)
        if eps <= 0 or not precision_is_sufficient(n, kappa, eps):
            return False
        return abs(center(a, j) - n) < eps
    except ZeroDivisionError:
        # Degenerate geometric coordinates reject. The nontorsion theorem
        # rules out this branch for the guarded indices of the fixed P.
        return False


def encode_signed(n):
    if type(n) is not int:
        raise TypeError("ordinary integer required")
    return 2 * n if n >= 0 else -2 * n - 1


def decode_signed(code):
    if type(code) is not int or code < 0:
        raise ValueError("natural-number code required")
    return code // 2 if code % 2 == 0 else -(code // 2) - 1


def accepts_naturals(n, kappa, a, ell, j):
    """Fixed natural-number input convention for a future DPRM translation."""
    return accepts(*(decode_signed(code) for code in (n, kappa, a, ell, j)))


if __name__ == "__main__":
    import argparse
    import json
    import sys

    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--natural", action="store_true",
                        help="decode each input by the fixed signed-integer bijection")
    parser.add_argument("indices", nargs=5, type=int, metavar="INTEGER")
    arguments = parser.parse_args()
    predicate = accepts_naturals if arguments.natural else accepts
    print(json.dumps({"accepted": predicate(*arguments.indices)}))
