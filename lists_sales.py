sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('enter new day data: ')
sales_w2.append(int(new_day))
sales = sales_w1 + sales_w2
sales.sort()
worst_day_sales = min(sales) * 1.5
best_day_sales = max(sales) * 1.5
print(f'worst day profit: {worst_day_sales}')
print(f'best day profit: {best_day_sales}')
print(f'combined profit: {worst_day_sales + best_day_sales}')



