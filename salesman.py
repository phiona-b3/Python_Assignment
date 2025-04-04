import numpy as np

def sales_report_with_numpy():
    salesmen_names = []
    sales_array = np.zeros((10, 5))  # 10 salesmen, 5 items

    # Input names and sales
    for i in range(10):
        name = input(f"\nEnter name of salesman #{i+1}: ")
        salesmen_names.append(name)

        print("Enter sales for 5 items:")
        for j in range(5):
            while True:
                try:
                    sales_array[i][j] = float(input(f"  Item{j+1} sale: "))
                    break
                except ValueError:
                    print("  Invalid input! Please enter a number.")

    # Calculate total per salesman and grand total
    total_per_salesman = np.sum(sales_array, axis=1)
    grand_total = np.sum(sales_array)

    # Print Report
    print("\nSales Report:")
    print("Name\t\tItem1\tItem2\tItem3\tItem4\tItem5\tTotalSales")
    print("--------------------------------------------------------------")
    
    for i in range(10):
        item_sales = "\t".join(f"{sales_array[i][j]:.0f}" for j in range(5))
        print(f"{salesmen_names[i]:<10}\t{item_sales}\t{total_per_salesman[i]:.0f}")

    print("--------------------------------------------------------------")
    print(f"Grand Total:\t\t\t\t\t\t{grand_total:.0f}")

# Run the function
sales_report_with_numpy()
