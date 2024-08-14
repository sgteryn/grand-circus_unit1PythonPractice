import math

print("Hello console!")

my_name = "Teryn Milliner"
work_from_home = True
side = 15
radius = 10

print("My name is" + my_name)
print("I work from home: " + str(work_from_home))
print(f"The length of each side is {side}")
txt = "The radius of the circle is {}"
print(txt.format(radius))

square_area = side * side
square_perimeter = 4 * side
circle_area = math.pi * radius * radius
circle_perimeter = math.pi * 2 * radius
print(f"The square area is {square_area} and the perimeter is {square_perimeter}")
print(f"The circle area is {circle_area} and the perimeter is {circle_perimeter}")