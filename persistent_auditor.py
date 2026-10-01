INVENTORY_FILE = "inventory.txt"


def load_inventory():

    try:
        with open(INVENTORY_FILE, "r") as f:
            lines = f.readlines()

        total_inventory = 0
        history_list = []

        for line in lines:
            line = line.strip()
            if line.startswith("Total:"):
                total_inventory = int(line.split(":", 1)[1].strip())
            elif line.startswith("History:"):
                history_part = line.split(":", 1)[1].strip()
                if history_part:
                    history_list = [int(x) for x in history_part.split(",")]

        return total_inventory, history_list

    except FileNotFoundError:
       
        return 0, []


def get_valid_input():
    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()
    if user_input.lower() == "quit":
        return "quit"
    if not user_input.isdigit():
        print("Invalid input: Please enter a positive integer.")
        return None
    return int(user_input)


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    tax_rate = 0.10
    return amount * tax_rate


def generate_report(total_units, deliveries_processed, failed_attempts):
    print(f"Total Units Processed: {total_units}")
    print(f"Total Deliveries Processed: {deliveries_processed}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    # Phase A check: load whatever was saved, or start empty if no file exists.
    total_inventory, history_list = load_inventory()
    print(f"Loaded -> Total: {total_inventory}, History: {history_list}")

    deliveries_processed = 0
    failed_entries = 0

    while True:
        result = get_valid_input()

        if result == "quit":
            generate_report(total_inventory, deliveries_processed, failed_entries)
            break

        if result is None:
            failed_entries += 1
            continue

        quantity = result
        tax = calculate_tax(quantity)
        total_inventory = process_delivery(total_inventory, quantity)
        deliveries_processed += 1
        print(f"Delivery accepted: {quantity} units | Tax on this delivery: {tax:.2f}")


if __name__ == "__main__":
    main()