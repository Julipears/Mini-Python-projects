import pandas as pd

time_tracker = pd.read_pickle("curr_times.pkl")

print("The current time tracker is:")
print(time_tracker)

newWeek = input("Is it a new week? (Y/N) ")
if newWeek == "Y":
  coursework = {"Sunday": [0]*6, "Monday": [0]*6, "Tuesday": [0]*6, "Wednesday": [0]*6, "Thursday": [0]*6, "Friday": [0]*6, "Saturday": [0]*6}
  time_tracker = pd.DataFrame(coursework, index=["BME205","ECE259","ECE286","ESC204","JRE410","PHY294"])
  
dayOfWeek = input("What day is it? (Enter 'Done' if done logging) ")

while dayOfWeek != "Done":
  time_tracker = pd.read_pickle("curr_times.pkl")
  
  courseLogged = input("What course is this for? (If entered wrong date, enter 'Back') ")
  if courseLogged == "Back":
    pass
  if courseLogged not in time_tracker.index:
    print("Course invalid")
    continue

  currTime = time_tracker.at[courseLogged, dayOfWeek]
  addTime = input("How many more hours did you spend on this course? ")
  addTime = float(addTime)

  totTime = currTime + addTime
  time_tracker.at[courseLogged, dayOfWeek] = totTime
  
  print(time_tracker)

  time_tracker.to_pickle("curr_times.pkl")

  newWeek = input("Is it a new week? (Y/N) ")
  if newWeek == "Y":
    time_tracker = time_tracker.replace(time_tracker, 0)
  
  dayOfWeek = input("What day is it? (Enter 'Done' if done logging) ")
