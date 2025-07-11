# tire_volume.py
# Enhancement: This program estimates the tire volume, suggests a price based on tire size,
# and records user's phone number if they are interested in buying.

import math
from datetime import datetime

# Get user input
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the volume using the given formula
volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
volume = round(volume, 2)

# Display the result
print(f"The approximate volume is {volume} liters")

# Optional: Check for price suggestion based on known sizes
price = None
if width == 205 and aspect_ratio == 60 and diameter == 15:
    price = 45000
elif width == 185 and aspect_ratio == 50 and diameter == 14:
    price = 37000
elif width == 225 and aspect_ratio == 65 and diameter == 17:
    price = 62000
elif width == 195 and aspect_ratio == 55 and diameter == 16:
    price = 42000

if price:
    print(f"Estimated price for this tire size: ₦{price}")

# Ask if the user wants to buy tires
buy_choice = input("Do you want to buy tires with these dimensions? (yes/no): ").strip().lower()
phone_number = ""
if buy_choice == "yes":
    phone_number = input("Please enter your phone number: ")

# Get current date
current_date = datetime.now().striftime("%Y-%m-%d")

# Write to volumes.txt
with open("volumes.txt", "at") as file:
    if phone_number:
        file.write(f"{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume}, {phone_number}\n")
    else:
        file.write(f"{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume}\n")
