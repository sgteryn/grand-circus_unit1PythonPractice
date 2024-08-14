import math

print("Hello World!")

my_name = "Teryn Milliner"
work_from_home = True
side = 15
radius = 10

square_area = side * side
square_perimeter = 4 * side
circle_area = math.pi * radius * radius
circle_perimeter = 2 * math.pi * radius


print("My name is " + my_name)
txt = "I work from home: {}"
print(txt.format(work_from_home))
print(f"The length of each side the square is {side}")
print("The radius of the circle is " + str(radius))

print(f"The square area is {square_area} and the perimeter is {square_perimeter}")
print(f"The circle area is {circle_area} and the perimeter is {circle_perimeter}")

travel_options = ["foot", "bike", "car", "airplane"]

print(f"1) {travel_options[0]}")
print(f"2) {travel_options[1]}")
print(f"3) {travel_options[2]}")
print(f"4) {travel_options[3]}")


travel_type = input("How would you like to travel? ")

distance = 100

time = 0

cost = 0

if travel_type == "foot":
    print("Walking is free! Speed is 3mph.")
    cost = 0
    time = distance / 3

elif travel_type == "bike":
    rent_bike = input("Do you need to rent a bike? (yes or no) ")
    if rent_bike == "yes":
        print("Bike rental is $45! Speed is 10pmh.")
        cost = 45
    else:
        print("Biking is free! Speed is 10mph.")
        cost = 0
    time = distance / 10

elif travel_type == "car":
    print("Driving is $0.25/mi. Speed is 60mph.")
    cost = 0.25 * distance
    time = distance / 60

elif travel_type == "airplane":
    print("Flying is $0.10/mi. Speed is 400mph.")
    passenger_count = int(input("How many passengers? "))
    cost = 0.10 * distance * passenger_count
    time = distance / 400

else:
    print(f"Sorry. {travel_type} is an invalid option.")

print(f"Traveling {distance} miles by {travel_type} took {time} hours and cost ${cost}.")

cost_bar = "Cost: "
for c in range(1, math.ceil(cost)):
    cost_bar += "$"

time_bar = "Time: "
for t in range(0, math.ceil(time)):
    time_bar += "/"

print(time_bar)
print(cost_bar)


