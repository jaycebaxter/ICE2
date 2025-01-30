#####################################################################################
# Program: Temperature Sensor
# Author: Jayce Baxter
# Date: January 28th, 2025
# Description: Calculates minimum, maximum and average temperature based on
#              user input
#####################################################################################

temp = []

validation = False

numeric_value = False
valid_range = False
list_populated = False
user_exit = False

if list_populated == True and valid_range == True and numeric_value == True and user_exit == True:
    validation = True

while user_exit == False:
    menu_option = input("Enter 1 to add a temperature, 2 to calculate, or 3 to exit: ")

    try:
        menu_option = int(menu_option)

    except ValueError:
        print("Please enter a number.")
        continue

    if menu_option == 1:
        # add temp
        while validation == False:
            user_temp = input("\nPlease enter a temperature, or enter q to return to menu: ")

            if user_temp == "":
                print("Input cannot be blank.")
                continue

            try:
                user_temp = float(user_temp)
                numeric_value = True

            except ValueError:
                if user_temp == "q":
                    break
                else:
                    print("Please enter a valid number.")
                    continue

            if user_temp < -50 or user_temp > 150:
                print("Temperature must be between -50 and 150 degrees Celsius.")
                continue
            else:
                temp.append(user_temp)
                valid_range = True    

    elif menu_option == 2:
        temp_sum = sum(temp)
        temp_length = len(temp)
        average_temp = int(temp_sum) / int(temp_length)
        min_temp = min(temp)
        max_temp = max(temp)
        print(f"The average temperature is {round(average_temp, 2)}.")
        print(f"The minimum temperature is {round(min_temp, 2)}.")
        print(f"The maximum temperature is {round(max_temp, 2)}.")

    elif menu_option == 3:
        user_exit = True