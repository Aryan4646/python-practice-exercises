Year = int(input("Enter the year you want to check is leap year or not: "))

# A tropical year (the basis for our calendar year) is approximately 365.242 days.
# To simplify, we use 365.25 days in the Julian calendar, which leads to an error of about 0.008 days per year.
# This small error accumulates and results in one extra day roughly every 125 years (1 / 0.008 ≈ 125).
# The more accurate Gregorian calendar adjusts for this as follows:
# 365.242 ≈ 365 + 0.25 - 0.01 + 0.002
# - The 0.25 accounts for an extra day every 4 years (leap year).
# - The 0.01 is corrected by skipping a leap year every 100 years (years divisible by 100 are not leap years).
# - The 0.002 is adjusted by adding a leap year back every 400 years (years divisible by 400 are leap years).

if Year % 100 == 0:
    if Year % 400 == 0:
        print(f"{Year} is a leap year")
    else:
        print(f"{Year} is not a leap year")
elif Year % 4 == 0:
    print(f"{Year} is a leap year")
else:
    print(f"{Year} is not a leap year")

