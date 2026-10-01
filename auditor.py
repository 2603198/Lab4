def main():
    total_inventory = 0
    failed_entries = 0
    while True:
        user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()
        if user_input.lower() == "quit":
            print(f"Total Units Processed: {total_inventory}")
            print(f"Number of Failed/Rejected Entries: {failed_entries}")
            break
        if not user_input.isdigit():
            print("Invalid input: Please enter a positive integer.")
            failed_entries += 1
            continue
        quantity = int(user_input)
        if quantity < 0:
            print("Rejected: Negative numbers are not allowed.")
            failed_entries += 1
            continue
        total_inventory += quantity

        if total_inventory > 500:
            print("Alert: Inventory overstock! Exceeding 500 units.")
            break

main()