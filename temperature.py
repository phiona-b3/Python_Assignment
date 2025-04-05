def main():
    temperatures = []
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for day in days:
        temp = float(input(f"Enter the temperature for {day}: "))
        temperatures.append(temp)

    lowest = min(temperatures)
    highest = max(temperatures)
    total_sum = sum(temperatures)
    average = total_sum / len(temperatures)

    print(f"Lowest Temperature: {lowest:.2f}")
    print(f"Highest Temperature: {highest:.2f}")
    print(f"Total Temperature: {total_sum:.2f}")
    print(f"Average Temperature: {average:.2f}")

main()