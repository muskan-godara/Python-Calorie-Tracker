# ---------------------------------------------------------------------
# Project Title: Daily Calorie Tracker CLI
# Course       : Programming for Puthon Solving using Python
# Units Used   : Unit 1 (Basics) + Unit 2 (Lists, Strings, File I/O)
# Name         : Muskan
# Date         : 19th Oct 2025
# ---------------------------------------------------------------------

# Task 1: Setup & Introduction
print("==============================================")
print("🍎 Welcome to the Daily Calorie Tracker!🍎")
print("==============================================")
print("This simple Python program helps you record your meals,")
print("calculate total and average calories, and check if you're")
print("within your daily calorie limit.\n")

# Task 2: Input & Data Collection
meals = []           # List to store meal names
calories = []        # List to store calorie values

num_meals = int(input("How many meals did you have today? - "))

for i in range(num_meals):
    meal_name = input(f"Enter meal {i+1} name: ")
    cal = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(cal)

# Task 3: Calorie Calculations
total_cal = sum(calories)
avg_cal = total_cal / len(calories)
limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
print("\n------------------------------------------")
if total_cal > limit:
    print("⚠️ WARNING: You have exceeded your daily calorie limit!")
else:
    print("✅ Great! You are within your daily calorie limit.")
print("--------------------------------------------")

#Task 5: Neatly Formatted Output
print("\n============ 📄 Daily Calorie Report ====================")
print("Meal Name\tCalories")
print("-----------------------------------------------------------")
for i in range(len(meals)):
    print(f"{meals[i]}\t\t{calories[i]}")
print("-----------------------------------------------------------")
print(f"Total:\t\t{total_cal}")
print(f"Average:\t{avg_cal}")
print("===========================================================")

# Task 6 (Bonus): Save to File 
save = input("\nWould you like to save this report to a file? (yes/no): ").lower()

if save == "yes":
    file = open("calorie_log.txt", "w")
    file.write("==========Daily Calorie Tracker Log =========\n")
    file.write("Meal Name\tCalories\n")
    file.write("--------------------------------------------------\n")
    for i in range(len(meals)):
        file.write(f"{meals[i]}\t\t{calories[i]}\n")
    file.write("--------------------------------------------------")
    file.write(f"Total:\t\t{total_cal}\n")
    file.write(f"Average:\t\t{avg_cal}\n")
    if total_cal > limit:
        file.write("Status: Exceeded daily limit\n")
    else:
        file.write("Status: Within daily limit\n")
    file.write("==================================================")
    file.close()
    print("Report saved successfully as 'calorie_log.txt'!")
else:
    print("Report not saved. Thank you for using the tracker!")
print("\n🍏 Stay healthy and track your calories every day! 🍎")