
import csv
import os

from bill_calculator import calculate_bill


def generate_household_report(records, tariff):

    household_records = {}

    # Group records by household
    for record in records:

        house = record["house_id"]

        if house not in household_records:
            household_records[house] = []

        household_records[house].append(record)

    report_data = []

    for house, house_records in household_records.items():

        house_records.sort(key=lambda x: x["month"])

        units = [
            int(record["units_consumed"])
            for record in house_records
        ]

        total_units = sum(units)
        average_units = total_units / len(units)

        highest_units = max(units)
        lowest_units = min(units)

        latest_record = house_records[-1]

        latest_units = int(latest_record["units_consumed"])

        estimated_bill = calculate_bill(latest_units, tariff)

        report_data.append({
            "house_id": house,
            "latest_month": latest_record["month"],
            "total_consumption": total_units,
            "average_consumption": round(average_units, 2),
            "highest_consumption": highest_units,
            "lowest_consumption": lowest_units,
            "latest_units": latest_units,
            "estimated_bill": estimated_bill["total_bill"]
        })

    return report_data


def export_report(records, tariff):

    report_data = generate_household_report(records, tariff)

    # Find project reports folder
    project_folder = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    reports_folder = os.path.join(project_folder, "reports")

    os.makedirs(reports_folder, exist_ok=True)

    file_path = os.path.join(
        reports_folder,
        "electricity_summary_report.csv"
    )

    fieldnames = [
        "house_id",
        "latest_month",
        "total_consumption",
        "average_consumption",
        "highest_consumption",
        "lowest_consumption",
        "latest_units",
        "estimated_bill"
    ]

    with open(file_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(report_data)

    print("\n===== REPORT GENERATED SUCCESSFULLY =====")
    print("Report saved at:")
    print(file_path)


def display_report(records, tariff):

    report_data = generate_household_report(records, tariff)

    print("\n===== HOUSEHOLD ELECTRICITY REPORT =====")

    for report in report_data:

        print("\nHousehold:", report["house_id"])
        print("Latest Month:", report["latest_month"])
        print("Total Consumption:", report["total_consumption"], "kWh")
        print("Average Consumption:", report["average_consumption"], "kWh")
        print("Highest Consumption:", report["highest_consumption"], "kWh")
        print("Lowest Consumption:", report["lowest_consumption"], "kWh")
        print("Latest Consumption:", report["latest_units"], "kWh")
        print("Estimated Latest Bill: Rs.", report["estimated_bill"])

        print("----------------------------------------")
