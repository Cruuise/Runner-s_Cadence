# File contains converstion function for times

# Function converts a string into seconds, returns seconds as an int
def str_to_seconds(time_str):
    # time_str expected to be in format "00:00:00" -> hours, minutes, seconds
    time_arr = time_str.split(":")
    time_arr = reversed(time_arr)
    total_seconds = 0
    for count,times in enumerate(time_arr):
        total_seconds += int(times) * (60 ** count)
    return total_seconds

# Function converts seconds to formatted string of time, ex. 01:12:02
def seconds_to_str(seconds):
    # power will increase by 60 if we have any hours or minutes
    # time_len helps format the list of values -> fixed an earlier division zero bug
    time_arr = []
    power = 0
    time_len = 1
    # Checks if we have any hours
    if seconds >= 3600:
        time_len = 3
        power = 3600
    # Checks if we have any minutes\
    elif seconds >= 60:
        time_len = 2 
        power = 60
    for count in range(time_len):
        current_value = int(seconds//power)
        time_arr.append(str(current_value).zfill(2))
        seconds -= current_value * power
        power /= 60
        print(f"seconds left: {seconds}")
    time = ':'.join(time_arr)
    # print(time_arr)
    # print(time)
    return time

# returns average mile time in seconds
def avg_mile_time(time: int, dist: float) -> float:
    if dist < 1.0:
        # increase it to 1 here
        # FOR TESTING PURPOSES REURN LARGE NUM
        return 99999.0
    return float(time/dist)
    # divide time by distance, return that (maybe make it round up and then turn it into int if required)


# Assume "1:02:3"
# Testing functions -> DELETE LATER
test = [1, 2, 3]
print(str_to_seconds("0:15:10"))
print(seconds_to_str(612))
avg = avg_mile_time(910,2)
avg = seconds_to_str(avg)
print(f"mile time is: {avg}")