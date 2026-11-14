
from datetime import datetime
from bill_calculator import calculate_bill


def forecast_next_month(records, history_months=3):

    household_records = {}

    # Group records by household
    for record in records:
        house = record["house_id"]

        if house not in household_records:
            household_records[house] = []

        household_records[house].append(record)

    forecasts = []

    for house, house_records in household_records.items():

        # Sort records by month
        house_records.sort(key=lambda x: x["month"])

        # Check if enough historical records exist
        if len(house_records) < history_months:
            continue

        # Get the latest 3 months
        recent_records = house_records[-history_months:]

        recent_units = [
            int(record["units_consumed"])
            for record in recent_records
        ]

        # Calculate average consumption
        average_units = sum(recent_units) / len(recent_units)

        predicted_units = round(average_units)

        # Calculate the next month
        last_month = house_records[-1]["month"]

        last_date = datetime.strptime(last_month, "%Y-%m")

        year = last_date.year
        month = last_date.month + 1

        if month > 12:
            month = 1
            year += 1

        next_month = f"{year}-{month:02d}"

        forecasts.append({
            "house_id": house,
            "forecast_month": next_month,
            "average_units": round(average_units, 2),
            "predicted_units": predicted_units
        })

    return forecasts


def display_forecast(records, tariff):

    forecasts = forecast_next_month(records)

    print("\n===== ELECTRICITY BILL FORECAST =====")

    if not forecasts:
        print("Not enough historical records for forecasting.")
        return

    for forecast in forecasts:

        units = forecast["predicted_units"]

        estimated_bill = calculate_bill(units, tariff)

        print("\nHousehold:", forecast["house_id"])
        print("Forecast Month:", forecast["forecast_month"])
        print("Average Consumption:", forecast["average_units"], "kWh")
        print("Predicted Consumption:", units, "kWh")

        print(
            "Estimated Electricity Bill: Rs.",
            estimated_bill["total_bill"]
        )

        print("--------------------------------------")
