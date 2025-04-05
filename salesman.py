def sales():
    num_salesmen = 10
    num_items = 5

    salesmen_data = []
    grand_total = 0

    for i in range(num_salesmen):
        name = input(f"\nEnter name of salesman {i + 1}: ")
        print("Enter sales for 5 items separated by spaces (e.g. 10 20 15 30 25):")
        sales = list(map(float, input("→ ").split()))

        while len(sales) != 5:
            print("❗ Please enter exactly 5 numbers.")
            sales = list(map(float, input("→ ").split()))

        total = sum(sales)
        grand_total += total
        salesmen_data.append((name, sales, total))

    print("\nName\tItem1\tItem2\tItem3\tItem4\tItem5\tTotal")
    print("------------------------------------------------------------")

    for entry in salesmen_data:
        name, sales, total = entry
        sales_str = '\t'.join(str(int(s)) for s in sales)
        print(f"{name}\t{sales_str}\t{int(total)}")

    print("------------------------------------------------------------")
    print(f"GrandTotal:\t\t\t\t\t\t{int(grand_total)}")

sales()
