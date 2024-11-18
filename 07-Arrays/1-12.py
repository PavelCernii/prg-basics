categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_exp_index = expenses.index(max(expenses))
print('The most expensive category is:', categories[max_exp_index])
print('Amount:', expenses[max_exp_index])