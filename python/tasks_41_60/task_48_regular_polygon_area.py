import math

side_count, side_length = map(int, input("in: ").split(", "))

single_triangle_area = side_length ** 2 / (4 * math.tan(math.pi / side_count))
regular_polygon_area = side_count * single_triangle_area

print(f"out: {regular_polygon_area}")
