def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("The triangle is a right triangle.")
    else:
        print("The triangle is not a right triangle.")

# Example usage
is_right_triangle(3, 4, 5)