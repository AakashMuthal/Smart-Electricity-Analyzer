
# ==========================================
# SMART ELECTRICITY CONSUMPTION ANALYZER
# STEP 05 - ANOMALY DETECTION
# ==========================================


# 1. Detect unusual electricity consumption
def detect_anomalies(
    records,
    min_history=3,
    warning_multiplier=1.5,
    critical_multiplier=2.0
):

    anomalies = []

    # Group records by household
    household_records = {}

    for record in records:

        house = record["house_id"]

        if house not in household_records:
            household_records[house] = []

        household_records[house].append(record)

    # Analyze each household separately
    for house, house_records in household_records.items():

        # Sort records chronologically
        house_records.sort(key=lambda x: x["month"])

        historical_units = []

        for record in house_records:

            current_units = int(record["units_consumed"])

            # Need enough previous records
            if len(historical_units) >= min_history:

                average = sum(historical_units) / len(historical_units)

                warning_limit = average * warning_multiplier
                critical_limit = average * critical_multiplier

                if current_units >= critical_limit:

                    status = "CRITICAL"

                elif current_units >= warning_limit:

                    status = "WARNING"

                else:

                    status = "NORMAL"

                increase = (
                    (current_units - average) / average
                ) * 100 if average > 0 else 0

                # Save unusual records
                if status != "NORMAL":

                    anomalies.append({
                        "house_id": house,
                        "month": record["month"],
                        "units": current_units,
                        "historical_average": round(average, 2),
                        "increase_percentage": round(increase, 2),
                        "status": status
                    })

            # Add current usage to history
            historical_units.append(current_units)

    return anomalies


# 2. Display anomaly report
def display_anomaly_report(records):

    if not records:
        print("\nNo electricity records available.")
        return

    anomalies = detect_anomalies(records)

    print("\n")
    print("=" * 60)
    print("       ELECTRICITY ANOMALY DETECTION REPORT")
    print("=" * 60)

    if not anomalies:

        print("\nNo unusual electricity consumption detected.")

        print("=" * 60)
        return

    critical_count = 0
    warning_count = 0

    for item in anomalies:

        print("\nHouse ID:", item["house_id"])
        print("Month:", item["month"])
        print("Consumption:", item["units"], "kWh")

        print(
            "Historical Average:",
            item["historical_average"],
            "kWh"
        )

        print(
            "Consumption Increase:",
            item["increase_percentage"],
            "%"
        )

        print("Status:", item["status"])

        print("-" * 60)

        if item["status"] == "CRITICAL":
            critical_count += 1

        elif item["status"] == "WARNING":
            warning_count += 1

    print("\n========== SUMMARY ==========")

    print("Total Anomalies:", len(anomalies))
    print("Critical Cases:", critical_count)
    print("Warning Cases:", warning_count)

    print("=" * 60)
