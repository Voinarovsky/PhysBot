def equation_ellipse(x1, y1, a, b, c, e):
    t = a * a + b * b
    a1 = t - e * (a * a)
    b1 = t - e * (b * b)
    c1 = (-2 * t * x1) - (2 * e * c * a)
    d1 = (-2 * t * y1) - (2 * e * c * b)
    e1 = -2 * e * a * b
    f1 = (-e * c * c) + (t * x1 * x1) + (t * y1 * y1)

    print("Equation of ellipse is", a1, "x^2 +", b1, "y^2 +",
          c1, "x +", d1, "y +", e1, "xy +", f1, "= 0")


# Driver Code
if __name__ == "__main__":
    x1, y1, a, b, c, e = 1, 1, 1, -1, 3, 0.5 * 0.5

    equation_ellipse(x1, y1, a, b, c, e)