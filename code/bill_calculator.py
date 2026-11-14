
import json
import os

# ==========================================
# ELECTRICITY BILL CALCULATOR
# STEP 04
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

TARIFF_FILE = os.path.join(
    BASE_DIR,
    "data",
    "tariff_settings.json"
)


# 1. Load tariff settings
def load_tariff():

    try:
        with open(TARIFF_FILE, "r") as file:
            tariff = json.load(file)

        return tariff

    except FileNotFoundError:
        print("Tariff settings file not found!")
        return None

    except json.JSONDecodeError:
        print("Invalid tariff settings JSON!")
        return None


# 2. Calculate electricity energy charges
def calculate_energy_charge(units, slabs):

    if units < 0:
        raise ValueError("Units cannot be negative.")

    remaining_units = units
    previous_limit = 0
    energy_charge = 0

    for slab in slabs:

        limit = slab["limit"]
        rate = slab["rate"]

        if rate < 0:
            raise ValueError("Tariff rate cannot be negative.")

        if limit is None:

            slab_units = remaining_units

        else:

            if limit <= previous_limit:
                raise ValueError("Tariff slabs must have increasing limits.")

            slab_capacity = limit - previous_limit
            slab_units = min(remaining_units, slab_capacity)

        energy_charge += slab_units * rate
        remaining_units -= slab_units

        if remaining_units <= 0:
            break

        if limit is not None:
            previous_limit = limit

    if remaining_units > 0:
        raise ValueError("Tariff slabs do not cover all consumption.")

    return round(energy_charge, 2)


# 3. Calculate complete electricity bill
def calculate_bill(units, tariff):

    energy_charge = calculate_energy_charge(
        units,
        tariff["slabs"]
    )

    fixed_charge = tariff["fixed_charge"]

    additional_rate = tariff["additional_charge_rate"]

    additional_charge = energy_charge * additional_rate

    total_bill = (
        energy_charge
        + fixed_charge
        + additional_charge
    )

    return {
        "units": units,
        "energy_charge": round(energy_charge, 2),
        "fixed_charge": round(fixed_charge, 2),
        "additional_charge": round(additional_charge, 2),
        "total_bill": round(total_bill, 2)
    }


# 4. Display electricity bill
def display_bill(records, tariff):

    if not records:
        print("\nNo electricity records available.")
        return

    if tariff is None:
        print("\nCannot calculate bill without tariff settings.")
        return

    house_id = input("\nEnter House ID: ").strip()

    month = input("Enter Month (YYYY-MM): ").strip()

    selected_record = None

    for record in records:

        if (
            record["house_id"].strip().lower() == house_id.lower()
            and record["month"] == month
        ):
            selected_record = record
            break

    if selected_record is None:

        print("\nNo matching electricity record found!")
        return

    units = int(selected_record["units_consumed"])

    bill = calculate_bill(units, tariff)

    print("\n")
    print("=" * 45)
    print("          ELECTRICITY BILL")
    print("=" * 45)

    print("House ID:", house_id)
    print("Billing Month:", month)
    print("Units Consumed:", units, "kWh")

    print("-" * 45)

    print("Energy Charges: Rs.", bill["energy_charge"])
    print("Fixed Charges: Rs.", bill["fixed_charge"])
    print("Additional Charges: Rs.", bill["additional_charge"])

    print("-" * 45)

    print("TOTAL BILL: Rs.", bill["total_bill"])

    print("=" * 45)


# 5. Display bills for all records
def display_all_bills(records, tariff):

    if not records:
        print("\nNo records available.")
        return

    if tariff is None:
        print("\nCannot calculate bills without tariff settings.")
        return

    total_amount = 0

    print("\n========== HOUSEHOLD BILL SUMMARY ==========")

    for record in records:

        units = int(record["units_consumed"])

        bill = calculate_bill(units, tariff)

        total_amount += bill["total_bill"]

        print(
            record["house_id"],
            "|",
            record["month"],
            "|",
            units,
            "units | Rs.",
            bill["total_bill"]
        )

    print("-" * 50)

    print("Total Estimated Billing Amount: Rs.", round(total_amount, 2))
