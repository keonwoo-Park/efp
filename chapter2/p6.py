from datetime import date

day = date.today()
current_year = day.year

age = input("What is your current age?")
retire = input("At what age would like to retire?")

work_day = int(retire) - int(age)
retire_year = day.replace(day.year + work_day).year

print("You have %d years left until you can retire." % (work_day) )
print("It's %s, so you can retire in %s." % (current_year, retire_year) )
