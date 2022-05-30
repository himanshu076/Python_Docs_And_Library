
# *abs()

# *it always gives a absolute value means +ive & for complex it gives magnitude

# floating point number
# float = -54.26
# print('Absolute value of float is:', abs(float))

# # An integer
# int = -94
# print('Absolute value of integer is:', abs(int))

# # A complex number
# complex = (3 - 4j)
# print('Absolute value or Magnitude of complex is:', abs(complex))

# ----------------------------------------------------------------------------------------------------------------------------------
# *Examples


# Python3 Program to calculate speed,
# distance and time

# Function to calculate speed
def cal_speed(dist, time):
    print(" Distance(km) :", dist)
    print(" Time(hr) :", time)
    return dist / time

# Function to calculate distance traveled
def cal_dis(speed, time):
    print(" Time(hr) :", time)
    print(" Speed(km / hr) :", speed)
    return speed * time

# Function to calculate time taken
def cal_time(dist, speed):
    print(" Distance(km) :", dist)
    print(" Speed(km / hr) :", speed)
    return speed * dist


# Driver Code
# Calling function cal_speed()
print(" The calculated Speed(km / hr) is :",
      cal_speed(abs(45.9), abs(2.0)))
print("")

# Calling function cal_dis()
print(" The calculated Distance(km) :",
      cal_dis(abs(62.9), abs(2.5)))
print("")

# Calling function cal_time()
print(" The calculated Time(hr) :",
      cal_time(abs(48.0), abs(4.5)))
