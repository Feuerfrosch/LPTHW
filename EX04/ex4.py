# assigns the value of 100 to the variable "cars"
cars = 100
# assigns the value of 4.0 (floating point number) to the variable "space in a car"
space_in_a_car = 4.0
# assigns 30 to the variable "drivers"
drivers = 30
# assigns the variable "passengers" the value 90
passengers = 90
# defines the variable "cars_not_driven" by subtracting two other variables
cars_not_driven = cars - drivers
# defines the variable "cars_driven" by making it equal to another variable
cars_driven = drivers
# defines "carpool_capacity" by multiplying two other variables
carpool_capacity = cars_driven * space_in_a_car
# defines "average_passengers_per_car" by dividing two other variables
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
