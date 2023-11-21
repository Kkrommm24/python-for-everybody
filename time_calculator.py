
def add_time(start, duration, day = None):
  time, period = start.split(" ")
  hour, min = map(int, time.split(":"))
  add_hour, add_min = map(int, duration.split(":"))
  period = period.strip().upper()
  new_hour = hour + add_hour
  new_min = min + add_min
  n = 0
  if period == "AM":
    if (min + add_min >= 60 ):
      hour += int(new_min / 60)
      new_min = new_min % 60
    if hour + add_hour == 24:
        new_hour = 12
        return f"{new_hour}:{new_min} (next day)"
    elif hour + add_hour > 24:
        while(new_hour > 24):
            new_hour = hour + add_hour - 24 * n
            n += 1
        if(new_hour > 12): 
            new_hour = new_hour - 12
            period = "PM"
            return f"{new_hour}:{new_min} {period} ({n} days later)"
        return f"{new_hour}:{new_min} {period} ({n} days later)"
      
print(add_time("11:43 AM", "115:02"))