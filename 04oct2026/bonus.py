performance_rating = float(input("enter performance rating:"))
years_completed = float(input("enter years completed in company"))
if performance_rating >= 4 and years_completed >=2:
    print("eligible for bonus.")
else:
    print("not eligible for a bonus.")