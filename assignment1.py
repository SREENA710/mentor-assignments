# Coding Question: Next Working Day (N Days Ahead)
# ❓ Problem Statement
# Given:
# A starting day of the week (e.g., "Monday")
# An integer N representing the number of working days to move forward
# Write a function to return the day of the week after N working days, skipping weekends (Saturday and Sunday).
# 📌 Rules
# Working days: Monday to Friday
# Skip weekends entirely (they should not be counted)
# Input day is guaranteed to be valid ("Monday" to "Sunday")
# 📥 Input
# start_day (string): Starting day of the week
# n (int): Number of working days to add
# 📤 Output
# Return the resulting day of the week


# def find_day_after_n_working_days(start_day, n):
#     working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

#     if start_day == "Saturday" or start_day == "Sunday":
#         current_day = "Monday"   
#     else:
#         current_day = start_day

#     current_index = working_days.index(current_day)

#     result_index = (current_index + n) % len(working_days)
#     return working_days[result_index]
# print(find_day_after_n_working_days("Thursday", 3))
# print(find_day_after_n_working_days("Sunday", -3))  


def find_day_after_n_working_days(start_day, n):
    start_day = start_day.capitalize()

    working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    if start_day == "Saturday" or start_day == "Sunday":
        current_day = "Monday"
    else:
        current_day = start_day

    current_index = working_days.index(current_day)

    result_index = (current_index + n) % len(working_days)
    return working_days[result_index]


print(find_day_after_n_working_days("Thursday", 3))   
print(find_day_after_n_working_days("sunday", -3))   
print(find_day_after_n_working_days("FRIDAY", 2))    