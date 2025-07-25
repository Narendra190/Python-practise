from datetime import datetime, timedelta

# Input: starting date in YYYY-MM-DD format
start_date_str = input("Enter start date (YYYY-MM-DD): ")
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

sunday_count = 0

# Check each of the 13 days
for i in range(13):
    current_day = start_date + timedelta(days=i)
    if current_day.weekday() == 6:  # 6 = Sunday
        sunday_count += 1

print("Number of Sundays in 13 days:", sunday_count)
