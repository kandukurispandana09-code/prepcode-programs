YEAR = 360
MONTH = 30
n = int(input("enter number:"))
year = n// YEAR
month = (n% YEAR) // MONTH
day = (n% YEAR) % MONTH
print(f"result : {year} years{month} month{day}days")