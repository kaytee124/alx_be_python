task = input("Enter your task:")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: Your high-priority task '{task}' needs your attention soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: Your medium-priority task '{task}' is time-bound. Try to complete it on time.")
        else:
            print(f"Reminder: Your medium-priority task '{task}' can be scheduled accordingly.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: Your low-priority task '{task}' is time-bound. Don't forget to get to it eventually.")
        else:
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")