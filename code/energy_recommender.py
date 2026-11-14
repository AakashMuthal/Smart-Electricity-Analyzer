
def generate_recommendations(records):

    household_records = {}

    # Group records by household
    for record in records:
        house = record["house_id"]

        if house not in household_records:
            household_records[house] = []

        household_records[house].append(record)

    all_recommendations = []

    for house, house_records in household_records.items():

        # Sort records by month
        house_records.sort(key=lambda x: x["month"])

        units = [
            int(record["units_consumed"])
            for record in house_records
        ]

        average_units = sum(units) / len(units)
        latest_units = units[-1]

        recommendations = []

        # Rule 1: High electricity consumption
        if latest_units >= 300:
            recommendations.append(
                "High consumption detected. Reduce unnecessary appliance usage."
            )

        # Rule 2: Increasing consumption
        if len(units) >= 2 and units[-1] > units[-2]:
            increase = units[-1] - units[-2]

            if increase >= 50:
                recommendations.append(
                    "Electricity usage increased significantly. "
                    "Check AC, refrigerator and other high-power appliances."
                )

        # Rule 3: Consumption above household average
        if latest_units > average_units * 1.25:
            recommendations.append(
                "Current consumption is above your historical average. "
                "Monitor daily electricity usage."
            )

        # Rule 4: General energy-saving suggestions
        if latest_units >= 200:
            recommendations.append(
                "Use LED bulbs and switch off lights and fans when not needed."
            )

        # Rule 5: Low consumption
        if latest_units < 150:
            recommendations.append(
                "Good energy management! Continue your current saving habits."
            )

        # Default recommendation
        if not recommendations:
            recommendations.append(
                "Consumption looks stable. Continue monitoring your usage."
            )

        all_recommendations.append({
            "house_id": house,
            "latest_month": house_records[-1]["month"],
            "latest_units": latest_units,
            "average_units": round(average_units, 2),
            "recommendations": recommendations
        })

    return all_recommendations


def display_recommendations(records):

    results = generate_recommendations(records)

    print("\n===== ENERGY SAVING RECOMMENDATIONS =====")

    for result in results:

        print("\nHousehold:", result["house_id"])
        print("Latest Month:", result["latest_month"])
        print("Latest Consumption:", result["latest_units"], "kWh")
        print("Historical Average:", result["average_units"], "kWh")

        print("\nSuggestions:")

        for number, suggestion in enumerate(
            result["recommendations"], start=1
        ):
            print(f"{number}. {suggestion}")

        print("----------------------------------------")
