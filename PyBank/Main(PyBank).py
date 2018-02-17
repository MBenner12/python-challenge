import os
import csv

filename = input("budget_data_1.csv")
month_count = 0
revenue_total = 0
revenue_this_month = 0
revenue_last_month = 0
change_in_revenue = 0
changes_in_revenue = []
months = []

# open csv
filepath = os.path.join("raw_data", filename)
with open(filepath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

# Revenue Changes By Month
for row in csvreader:
    month_count = month_count + 1
    months.append(row[0])
    revenue_this_month = int(row[1])
    revenue_total = revenue_total + revenue_this_month
    if month_count > 1:
        change_in_revenue = revenue_this_month - revenue_last_month
        changes_in_revenue.append(revenue_change)
        revenue_last_month = revenue_this_month

# Month by Month Results
revenue_changes_sum = sum(changes_in_revenue)
avg_change = revenue_changes_sum / (month_count - 1)
max_change = max(changes_in_revenue)
min_change = min(changes_in_revenue)
max_month_index = changes_in_revenue.index(max_change)
min_month_index = changes_in_revenue.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

# Summary
print("Financial Summary")
print("------------------")
print(f"Total Months: {month_count}")
print(f"Revenue Total: ${revenue_total}")
print(f"Avg Revenue Change: ${avg_change}")
print(f"Largest Revenue Increase: {max_month} (${max_change})")
print(f"Largest Revenue Decrease: {min_month} (${min_change})")

# Summary txt
save_file = filename.strip(".csv") + "_results.txt"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as text:
    text.write("Financial Summary" + "\n")
    text.write("-----------------" + "\n")
    text.write(f"Total Months: {month_count}" + "\n")
    text.write(f"Revenue Total: ${revenue_total}" + "\n")
    text.write(f"Avg Revenue Change: ${avg_change}" + "\n")
    text.write(f"Largest Revenue Increase: {max_month} (${max_change})" + "\n")
    text.write(f"Largest Revenue Decrease: {min_month} (${min_change})" + "\n")