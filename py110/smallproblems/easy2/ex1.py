# P given an angle between 0 and 360, convert to degrees(minutes,seconds)
# assume floats are valid (only one decimal place)
# assume we round up
# E <-- see examples
# D

# temp_string
# temp_array
# d
# m
# s

# return sum
# A
# everything before decimal place is converted to a degree
# everything after the decimal case is a fraction of a decimal
# multiply by 60 --> and take first two digits --> that's minutes
# take next two digits, multiply by 60 --> that's seconds
# sum them all together
# C

DEGREE = "\u00B0"

def dms(my_float):
    result, remainder = divmod(my_float, 1)
    degrees = int(result)
    minutes = 0
    seconds = 0
    if (remainder != 0):
        temp_minutes = remainder * 60
        minutes, temp_seconds = divmod(temp_minutes, 1)
        minutes = int(minutes)
        seconds = int(temp_seconds * 60)
    result = f"{degrees}{DEGREE}{minutes:02d}\'{seconds:02d}\""
    return result

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")