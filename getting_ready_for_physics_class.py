# Getting Ready for Physics Class
# Use functions to calculate some fundamental physical properties.


# See "Use the Force"
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


print("Turn up the Temperature!")
# Equation to convert Fahrenheit to Celsius 
# temp (c) = (temp (f) - 32) * 5/9

# Use f_to_c function to convert Fahrenheit to Celsius.
def f_to_c(f_temp):
  return (f_temp - 32) * 5/9 

# test f_to_c function with a value of 100 Fahrenheit
f100_in_celsius = f_to_c(100)
print("100 fahrenheit converts to " + str(f100_in_celsius) + " celsius")
# converts to = 37.77777777777778 celsius

# Equation to convert Celsius to Fahrenheit 
# Temp (F) = Temp (C) * (9/5) + 32

# Use c_to_f function to convert Celsius to  Fahrenheit.
def c_to_f(c_temp):
  return (c_temp * 9/5) + 32
  
# test c_to_f function with a value of 0 Celsius
c0_in_fahrenheit = c_to_f(0)
print("0 celsius converts to " + str(c0_in_fahrenheit) + " fahrenheit")
# converts to 32.0 fahrenheit

print("Use the Force")
# get_force function
def get_force(mass, acceleration):
  return mass * acceleration

# Test get_force function
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.") 
# The GE train supplies 226800 Newtons of force.


# c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set c to have a default value of 3*10**8.

# get_energy function
def get_energy(mass, c=3*10**8):
  return mass * c**2

# test get_energy
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")
# A 1kg bomb supplies 90000000000000000 Joules.

# get_work function
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

# test get_work
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
# The GE train does 22680000 Joules of work over 100 meters.
