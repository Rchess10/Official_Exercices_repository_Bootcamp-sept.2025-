import datetime

# Ask for birthdate
birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")
day, month, year = map(int, birthdate_str.split('/'))

# Calculate age
today = datetime.date.today()
birthdate = datetime.date(year, month, day)
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Number of candles = last digit of age
candles = age % 10
if candles == 0:
    candles = 10  # If last digit is 0, show 10 candles

# Check for leap year
is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

def print_cake(candles):
    cake_width = max(17, candles + 6)
    candle_section = "_" * 3 + "i" * candles + "_" * 3
    top = candle_section.center(cake_width)
    happy = "|:H:a:p:p:y:|".center(cake_width)
    upper = "__|" + "_" * (cake_width - 4) + "|__"
    deco = "|" + "^" * (cake_width - 2) + "|"
    birthday = "|" + ":B:i:r:t:h:d:a:y:" + " " * (cake_width - 18) + "|"
    empty = "|" + " " * (cake_width - 2) + "|"
    bottom = "~" * cake_width

    print(top)
    print(happy)
    print(upper)
    print(deco)
    print(birthday)
    print(empty)
    print(bottom)

    # Print cakes
if is_leap:
    print_cake(candles)
    print()
    print_cake(candles)
else:
    print_cake(candles)