from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", current_date,)

def calculate_future_date(number_of_days):
    """Calculates and displays the future date after adding specified days."""
    future_date= timedelta(days=number_of_days)
    future_date= datetime.now() + future_date
    future_date= future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {future_date}")

days= int(input("Enter the number of days to add to the current date: "))
calculate_future_date(days)
display_current_datetime()
