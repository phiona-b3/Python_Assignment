def temperature_analysis():
    list_of_temp = [] #initialize an empty list

    for i in range(7):
        temp = float(input(f"Enter temperature for day {i+1}: "))
        list_of_temp.append(temp)

    # sorting to find min and max
    list_of_temp.sort()

    lowest_temp = list_of_temp[0]
    highest_temp = list_of_temp[-1]
    sum_of_temp = sum(list_of_temp)
    average_of_temp = sum_of_temp / len(list_of_temp)

    #Display results
    print("\nTemperature Analysis:")
    print(f"Lowest temperature: {lowest_temp:.2f}")
    print(f"Highest temperature: {highest_temp:.2f}")
    print(f"Sum of temperatures: {sum_of_temp:.2f}")
    print(f"Average temperature: {average_of_temp:.2f}")
temperature_analysis()