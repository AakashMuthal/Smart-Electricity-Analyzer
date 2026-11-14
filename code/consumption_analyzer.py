
# ==========================================
# SMART ELECTRICITY CONSUMPTION ANALYZER
# STEP 03 - CONSUMPTION ANALYSIS
# ==========================================


# 1. Calculate total electricity consumption
def calculate_total_consumption(records):

    total = 0

    for record in records:
        total += int(record["units_consumed"])

    return total


# 2. Calculate average consumption
def calculate_average_consumption(records):

    if not records:
        return 0

    total = calculate_total_consumption(records)

    return round(total / len(records), 2)


# 3. Find highest consumption record
def highest_consumption(records):

    if not records:
        return None

    highest = records[0]

    for record in records:

        if int(record["units_consumed"]) > int(highest["units_consumed"]):
            highest = record

    return highest


# 4. Find lowest consumption record
def lowest_consumption(records):

    if not records:
        return None

    lowest = records[0]

    for record in records:

        if int(record["units_consumed"]) < int(lowest["units_consumed"]):
            lowest = record

    return lowest


# 5. Calculate household-wise consumption
def household_consumption(records):

    household_data = {}

    for record in records:

        house = record["house_id"]
        units = int(record["units_consumed"])

        if house not in household_data:
            household_data[house] = 0

        household_data[house] += units

    return household_data


# 6. Calculate month-wise consumption
def monthly_consumption(records):

    monthly_data = {}

    for record in records:

        month = record["month"]
        units = int(record["units_consumed"])

        if month not in monthly_data:
            monthly_data[month] = 0

        monthly_data[month] += units

    return monthly_data


# 7. Calculate consumption growth percentage
def consumption_growth(records):

    monthly_data = monthly_consumption(records)

    months = sorted(monthly_data.keys())

    if len(months) < 2:
        return None

    previous_month = monthly_data[months[-2]]
    current_month = monthly_data[months[-1]]

    if previous_month == 0:
        return None

    growth = (
        (current_month - previous_month)
        / previous_month
    ) * 100

    return round(growth, 2)


# 8. Display complete consumption report
def display_analysis(records):

    if not records:
        print("\nNo records available for analysis.")
        return

    print("\n")
    print("=" * 55)
    print("       ELECTRICITY CONSUMPTION ANALYSIS")
    print("=" * 55)

    total = calculate_total_consumption(records)
    average = calculate_average_consumption(records)

    highest = highest_consumption(records)
    lowest = lowest_consumption(records)

    print("\n1. GENERAL CONSUMPTION STATISTICS")

    print("Total Units Consumed:", total, "kWh")
    print("Average Units Per Record:", average, "kWh")

    print("\n2. HIGHEST CONSUMPTION")

    print("House:", highest["house_id"])
    print("Month:", highest["month"])
    print("Units:", highest["units_consumed"], "kWh")

    print("\n3. LOWEST CONSUMPTION")

    print("House:", lowest["house_id"])
    print("Month:", lowest["month"])
    print("Units:", lowest["units_consumed"], "kWh")

    print("\n4. HOUSEHOLD-WISE CONSUMPTION")

    household_data = household_consumption(records)

    for house, units in household_data.items():

        print(house, ":", units, "kWh")

    print("\n5. MONTH-WISE CONSUMPTION")

    monthly_data = monthly_consumption(records)

    for month, units in sorted(monthly_data.items()):

        print(month, ":", units, "kWh")

    print("\n6. MONTHLY CONSUMPTION GROWTH")

    growth = consumption_growth(records)

    if growth is not None:

        print("Growth:", growth, "%")

    else:

        print("Not enough data to calculate growth.")

    print("\n" + "=" * 55)
