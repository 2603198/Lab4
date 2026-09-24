


def get_valid_input():

    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()

    if user_input.lower() == "quit":
        return "quit"

    if not user_input.isdigit():
        print("Invalid input: Please enter a positive integer.")
        return None

    quantity = int(user_input)
    if quantity < 0:

        print("Rejected: Negative numbers are not allowed.")
        return None

    return quantity


def process_delivery(current_total, new_value):

    new_total = current_total + new_value
    return new_total


def calculate_tax(amount):

    tax_rate = 0.10
    tax = amount * tax_rate
    return tax


def generate_report(total_units, deliveries_processed, failed_attempts):

    print(f"Total Units Processed: {total_units}")
    print(f"Total Deliveries Processed: {deliveries_processed}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    total_inventory = 0
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

        if total_inventory > 500:
            print("Alert: Inventory overstock! Exceeding 500 units.")
            generate_report(total_inventory, deliveries_processed, failed_entries)
            break


if __name__ == "__main__":
    main()
