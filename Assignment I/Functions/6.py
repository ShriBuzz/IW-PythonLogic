# Write a Python function to check whether a number is in a given range.

def check_range(num, lower_range, upper_range):
    if num in range(lower_range, upper_range):
        print("%s is in the range" % str(num))
    else:
        print("The number is outside the given range.")


check_range(8, 2, 10)
check_range(1, 2, 10)
