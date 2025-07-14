"""
CSC500-1 Module 5 Critical Thinking Part 1 - Rainfall Program
Lawrence Wilson
July 13, 2025
"""

from UserRainfall import UserRainfall

user_rainfall_obj = UserRainfall()

user_rainfall_obj.set_input_years()

years = user_rainfall_obj.get_years()

# Outer loop for each year and inner loop for each month within the year

for i in range(years):
    for j in range(12):
        user_rainfall_obj.set_rainfall()

total_rainfall_arr, total_rainfall = user_rainfall_obj.get_rainfall_data()

for index, monthly_rainfall in enumerate(total_rainfall_arr):
    print(f"Month {index + 1} Rainfall: {monthly_rainfall}")

print(f"Total rainfall: {total_rainfall}")
print("Average monthly rainfall inches:", end=' ')
print(f"{(total_rainfall/len(total_rainfall_arr) if len(total_rainfall_arr) > 0 else 0):.2f}")