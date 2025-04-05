sales_data = {}
grand_total = 0


for _ in range(10):
    
    name = input("Enter salesperson's name: ")


    sales = []


    for i in range(1, 6):
        sale = int(input(f"Enter sales for Item {i}: "))
        sales.append(sale)


    total_sales = sum(sales)


    sales_data[name] = (sales, total_sales)


    grand_total += total_sales


print("\nSales Report:")

print(f"{'Name':<15}{'Item1':<6}{'Item2':<6}{'Item3':<6}{'Item4':<6}{'Item5':<6}{'Total Sales':<10}")
print("-" * 60)

for name, (sales, total_sales) in sales_data.items():
    print(f"{name:<15}{sales[0]:<6}{sales[1]:<6}{sales[2]:<6}{sales[3]:<6}{sales[4]:<6}{total_sales:<10}")


print("-" * 60)
print(f"{'Grand Total':<15}{grand_total:<10}")
