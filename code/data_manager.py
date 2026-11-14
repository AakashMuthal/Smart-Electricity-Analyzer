
import csv
import os
from datetime import datetime

# Get project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset location
DATA_FILE = os.path.join(
    BASE_DIR,
    "data",
    "electricity_readings.csv"
)

# CSV columns
FIELDNAMES = [
    "house_id",
    "month",
    "previous_reading",
    "current_reading",
    "units_consumed"
]


# 1. Load electricity records

def load_records():

    import csv

    file_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "data",
        "electricity_readings.csv"
    )

    records = []

    with open(file_path, "r", newline="", encoding="utf-8-sig") as file:

        reader = csv.DictReader(file)

        for row in reader:

            clean_row = {
                key.strip(): value.strip() if isinstance(value, str) else value
                for key, value in row.items()
                if key is not None
            }

            records.append(clean_row)

    return records


# 2. Display electricity records
def display_records(records):

    if not records:
        print("\nNo records available.")
        return

    print("\n========== ELECTRICITY RECORDS ==========")

    for record in records:

        print(
            f"House: {record['house_id']} | "
            f"Month: {record['month']} | "
            f"Units: {record['units_consumed']}"
        )

    print("=========================================")


# 3. Validate new electricity reading
def validate_reading(house_id, month, previous, current, records):

    # Check house ID
    if not house_id.strip():
        return False, "House ID cannot be empty."

    # Check month format
    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        return False, "Invalid month! Use YYYY-MM format."

    # Check numeric readings
    try:
        previous = int(previous)
        current = int(current)
    except ValueError:
        return False, "Meter readings must be numbers."

    # Check reading values
    if previous < 0 or current < 0:
        return False, "Meter readings cannot be negative."

    if current <= previous:
        return False, "Current reading must be greater than previous reading."

    # Check duplicate records
    for record in records:

        if (
            record["house_id"].strip().lower() == house_id.strip().lower()
            and record["month"] == month
        ):
            return False, "This household already has a record for this month."

    return True, "Reading validated successfully."


# 4. Save records to CSV
def save_records(records):

    with open(DATA_FILE, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=FIELDNAMES
        )

        writer.writeheader()
        writer.writerows(records)

    print("\nRecords saved successfully!")


# 5. Add new electricity reading
def add_reading(records):

    print("\n========== ADD NEW READING ==========")

    house_id = input("Enter House ID: ").strip()
    month = input("Enter Month (YYYY-MM): ").strip()

    previous = input("Enter Previous Meter Reading: ")
    current = input("Enter Current Meter Reading: ")

    # Validate input
    valid, message = validate_reading(
        house_id,
        month,
        previous,
        current,
        records
    )

    if not valid:
        print("\nError:", message)
        return

    # Convert readings
    previous = int(previous)
    current = int(current)

    # Calculate units
    units = current - previous

    # Create new record
    new_record = {
        "house_id": house_id,
        "month": month,
        "previous_reading": previous,
        "current_reading": current,
        "units_consumed": units
    }

    records.append(new_record)

    # Save updated dataset
    save_records(records)

    print("\nReading added successfully!")
    print("Units consumed:", units)
