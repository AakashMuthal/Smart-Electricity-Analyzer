from data_manager import (
    load_records,
    display_records,
    add_reading
)

from consumption_analyzer import display_analysis

from bill_calculator import (
    load_tariff,
    display_bill,
    display_all_bills
)

from anomaly_detector import display_anomaly_report

from bill_forecaster import display_forecast

from energy_recommender import display_recommendations

from report_generator import (
    display_report,
    export_report
)


def display_menu():

    print("\n" + "=" * 50)
    print("       SMART ELECTRICITY CONSUMPTION ANALYZER")
    print("=" * 50)

    print("1. View Electricity Records")
    print("2. Add New Electricity Reading")
    print("3. Analyze Electricity Consumption")
    print("4. Calculate Electricity Bill")
    print("5. View All Household Bills")
    print("6. Detect Unusual Consumption")
    print("7. Forecast Next Month's Electricity Bill")
    print("8. Energy-Saving Recommendations")
    print("9. View Electricity Summary Report")
    print("10. Export Report to CSV")
    print("11. Exit")

    print("=" * 50)


def main():

    # Load electricity records
    records = load_records()

    # Load tariff settings
    tariff = load_tariff()

    if not records:
        print("No electricity records found.")
        return

    print("\nWelcome to Smart Electricity Analyzer!")

    while True:

        display_menu()

        choice = input("\nEnter your choice (1-11): ").strip()

        if choice == "1":

            display_records(records)

        elif choice == "2":

            add_reading(records)

        elif choice == "3":

            display_analysis(records)

        elif choice == "4":

            display_bill(records, tariff)

        elif choice == "5":

            display_all_bills(records, tariff)

        elif choice == "6":

            display_anomaly_report(records)

        elif choice == "7":

            display_forecast(records, tariff)

        elif choice == "8":

            display_recommendations(records)

        elif choice == "9":

            display_report(records, tariff)

        elif choice == "10":

            export_report(records, tariff)

        elif choice == "11":

            print("\nThank you for using Smart Electricity Analyzer!")
            print("Goodbye!")
            break

        else:

            print("\nInvalid choice! Please enter a number between 1 and 11.")


if __name__ == "__main__":
    main()
