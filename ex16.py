# datetime Library

from datetime import date, time, datetime, timedelta

def datetime_demo():

    print("1. Current Date")
    today = date.today()
    print("Today:", today)

    print("\n2. Create Date")
    custom_date = date(2025, 2, 10)
    print("Custom Date:", custom_date)

    print("\n3. Date Attributes")
    print("Year:", today.year)
    print("Month:", today.month)
    print("Day:", today.day)
    print("Weekday (0=Mon):", today.weekday())

    print("\n4. Create Time")
    custom_time = time(10, 30, 45)
    print("Custom Time:", custom_time)

    print("\n5. Current DateTime")
    now = datetime.now()
    print("Now:", now)

    print("\n6. Create DateTime")
    custom_datetime = datetime(2025, 2, 10, 10, 30, 0)
    print("Custom DateTime:", custom_datetime)

if __name__ == "__main__":
    datetime_demo()
