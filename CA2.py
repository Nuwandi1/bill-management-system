import datetime

class BillManagementSystem:
    shopName = ("***   Welcome to the TRENDY BUG   ***")  # Shop name
    shopaddress = ("45, Highlevel Rd, Nugegoda")  # Shop address
    shopcontact = ("011-3535353")  # Shop contact number

    # Printing shop details in the center of 75 characters
    print((65 * '=').center(75))
    print(shopName.center(75))
    print((65* '=').center(75))
    print(shopaddress.center(75))
    print(shopcontact.center(75))
    print()

    def __init__(self):
        self.bill_items = []  # List to store item details (product name, unit price, quantity, total price)
        self.total_list = []  # List to store total prices of each item
        self.sub_total = 0  # Initializing the sub-total of the bill to 0

    def add_bill_item(self, product_name, unit_price, quantity):
        total_price = unit_price * quantity  # Calculate total price for the current item
        self.total_list.append(total_price)  # Store the total price in the total_list
        self.bill_items.append((product_name, unit_price, quantity, total_price))  # Store item details in the bill_items list
        self.sub_total += total_price  # Update the sub-total by adding the current item's total price

    def calculate_total_with_discount(self, discount):
        return self.sub_total * (1 - discount / 100)  # Calculate the total bill amount after applying the discount

    def generate_bill_report(self, discount):
        print()
        print((65 * '-').center(75))
        print("Bill Report".center(75))  # Centering the "Bill Report" topic
        print((65 * '-').center(75))
        print()
        print("Date and Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # Print current date and time
        print("Product Name     Unit Price     Quantity     Total Price")
        print((75 * '-'))

        for item in self.bill_items:  # Iterate through each item in the bill_items list
            product_name, unit_price, quantity, total_price = item
            # Print item details in a formatted way
            print(
                f"{product_name:<12}     {unit_price:^10.2f}     {quantity:^8}     {total_price:>12.2f}"
            )
        print((75 * '-'))

        print(f"Sub Total: {self.sub_total:.2f}")  # Print the calculated sub-total

        if discount > 0:
            total_with_discount = self.calculate_total_with_discount(discount)
            print(f"Discount: {discount:.2f}%")  # Print the discount percentage
            print(f"Total Cost after Discount: {total_with_discount:.2f}")  # Print the final total after applying the discount
        else:
            print("No Discount Applied")
        print("THANK YOU, COME AGAIN!")  # Print a thank you message at the end

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))  # Get the input from the user and convert it to a float
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))  # Get the input from the user and convert it to an integer
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    bill_system = BillManagementSystem()  # Create an instance of the BillManagementSystem class

    while True:
        product_name = input("Enter the name of the item : ")

        unit_price = get_float_input("Enter the unit price: ")  # Get the unit price from the user
        quantity = get_int_input("Enter the quantity: ")  # Get the quantity from the user
        bill_system.add_bill_item(product_name, unit_price, quantity)  # Add the item to the bill

        option = input("Add another item to(y/n):")  # Ask the user if they want to add another item
        if option == "n":
            break  # Exit the loop if the user doesn't want to add more items

    print("")
    discount = get_float_input("Add discount: ")  # Get the discount from the user
    bill_system.generate_bill_report(discount)  # Generate the bill report with the given discount

if __name__ == "__main__":
    main()  # Call the main function to start the program



