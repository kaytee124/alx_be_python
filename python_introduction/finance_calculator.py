Monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

monthly_savings = Monthly_income - monthly_expenses

simple_interest =monthly_savings+ (monthly_savings * 5 * 12) / 100

print("Your monthly savings are:", monthly_savings)
print("Projected savings after 1 year, with interest, is:", simple_interest)