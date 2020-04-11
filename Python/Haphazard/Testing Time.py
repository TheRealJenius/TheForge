from time import time, sleep

start_time = time()
sleep(2.5)
end_time = time()
total_time=end_time-start_time
hours = int(total_time / 3600) # 3600 seconds in an hour
hourless = total_time % 3600
minutes = int(hourless / 60) # 60 seconds in a minute
seconds = round(hourless % 60) # rounding to the nearest second
print("Total Runtime = {}h:{}m:{}s".format(hours,minutes,seconds))