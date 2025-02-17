from chain import FoodChain


def display_menu():
    print("\n=== Food Delivery Blockchain System ===")
    print("1. Place New Order")
    print("2. View Pending Orders")
    print("3. Mine Orders Block")
    print("4. View Blockchain")
    print("5. Exit")
    return input("Select an option: ")

def main():
    food_chain = FoodChain()
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            customer = input("Enter customer name: ")
            restaurant = input("Enter restaurant name: ")
            items = []
            while True:
                item = input("Enter item (or 'done' to finish): ")
                if item.lower() == 'done':
                    break
                price = float(input("Enter item price: "))
                items.append({"item": item, "price": price})
            
            total_amount = sum(item["price"] for item in items)
            order_index = food_chain.add_order(customer, restaurant, items, total_amount)
            print(f"\nOrder added to pending transactions. Order ID: {order_index}")

        elif choice == '2':
            if not food_chain.pending_transactions:
                print("\nNo pending orders.")
            else:
                print("\nPending Orders:")
                for idx, order in enumerate(food_chain.pending_transactions, 1):
                    print(f"\nOrder {idx}:")
                    print(f"Customer: {order['customer']}")
                    print(f"Restaurant: {order['restaurant']}")
                    print("Items:")
                    for item in order['items']:
                        print(f"- {item['item']}: ${item['price']}")
                    print(f"Total Amount: ${order['total_amount']}")

        elif choice == '3':
            if not food_chain.pending_transactions:
                print("\nNo pending orders to mine.")
            else:
                new_block = food_chain.mine_pending_orders()
                print(f"\nNew block mined!")
                print(f"Block Hash: {new_block.hash}")
                print(f"Block Index: {new_block.index}")

        elif choice == '4':
            print("\nBlockchain:")
            for block in food_chain.chain:
                print(f"\nBlock #{block.index}")
                print(f"Hash: {block.hash}")
                print(f"Previous Hash: {block.previous_hash}")
                print(f"Timestamp: {block.timestamp}")
                if block.transactions:
                    print("Orders:")
                    for order in block.transactions:
                        print(f"\n- Customer: {order['customer']}")
                        print(f"  Restaurant: {order['restaurant']}")
                        print("  Items:")
                        for item in order['items']:
                            print(f"  - {item['item']}: ${item['price']}")
                        print(f"  Total Amount: ${order['total_amount']}")

        elif choice == '5':
            print("\nThank you for using the Food Delivery Blockchain System!")
            break

if __name__ == "__main__":
    main()