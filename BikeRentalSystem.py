class Bike:
    def __init__(self, bike_id, availability=True):
        self.bike_id = bike_id
        self.availability = availability

    def __str__(self):
        availability_status = 'Available' if self.availability else 'Not Available'
        return f"Bike {self.bike_id} - Availability: {availability_status}"


class RentalShop:
    def __init__(self):
        self.bikes = [Bike(bike_id) for bike_id in range(1, 6)]  # Initialize 5 bikes

    def view_available_bikes(self):
        print("Available Bikes:")
        for bike in self.bikes:
            print(bike)

    def rent_bike(self, bike_ids, rental_type, rental_time, is_family_rental, num_rentals):
        total_cost = 0

        for bike_id in bike_ids:
            bike = self.bikes[bike_id - 1]

            if bike.availability:
                bike.availability = False
                total_cost += self.calculate_rental_cost(rental_type, rental_time)

        if is_family_rental and 3 <= num_rentals <= 5:
            total_cost *= 0.8  # Apply 20% discount for the family deal

        return f"You have successfully rented bikes {', '.join(map(lambda x: str(x), bike_ids))}. Enjoy your ride and stay safe!\nTotal Cost: ${total_cost:.2f}"

    def return_bike(self, bike_ids, rentals_number, rental_type, rental_time, is_family_rental, num_rentals):
        total_cost = 0

        for bike_id in bike_ids:
            bike = self.bikes[bike_id - 1]

            if not bike.availability:
                bike.availability = True
                total_cost += self.calculate_rental_cost(rental_type, rental_time)

        if is_family_rental and 3 <= num_rentals <= 5:
            total_cost *= 0.8  # Apply 20% discount for the family deal

        return f"You have successfully returned bikes {', '.join(map(lambda x: str(x), bike_ids))}. Thank you for using our service!\nTotal Cost: ${total_cost:.2f}"

    def calculate_rental_cost(self, rental_type, rental_time):
        prices = {"hourly": 5, "daily": 10, "weekly": 50}
        base_cost = rental_time * prices[rental_type]

        return base_cost


class Customer:
    def __init__(self, name, lastname, age, phone):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.phone = phone

    def view_bike_menu(self, rental_shop):
        rental_shop.view_available_bikes()

    def rent_bike(self, rental_shop, bike_ids, rental_type, rental_time, is_family_rental=False, num_rentals=0):
        return rental_shop.rent_bike(bike_ids, rental_type, rental_time, is_family_rental, num_rentals)

    def return_bike(self, rental_shop, bike_ids, rentals_number, rental_type, rental_time, is_family_rental=False, num_rentals=0):
        return rental_shop.return_bike(bike_ids, rentals_number, rental_type, rental_time, is_family_rental, num_rentals)


if __name__ == "__main__":
    rental_shop = RentalShop()

    while True:
        print("\nWelcome to Bike Rental System. Please use numbers to navigate.")
        print("1. View Available Bikes")
        print("2. Rent Bike")
        print("3. Return Bike")
        print("4. Exit")

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            customer = Customer("", "", 0, "")  # Dummy customer for viewing available bikes
            customer.view_bike_menu(rental_shop)

        elif user_choice == "2":
            bike_ids = input("Enter the bike numbers you want to rent (e.g., 1 3 5): ").split()
            bike_ids = [int(bike_id) for bike_id in bike_ids]
            rental_type = input("Enter rental type (hourly, daily, weekly): ")
            rental_time = int(input("Enter rental time: "))
            
            customer_name = input("Enter your first name: ")
            customer_lastname = input("Enter your last name: ")
            customer_age = int(input("Enter your age: "))
            customer_phone = input("Enter your phone number: ")

            customer = Customer(customer_name, customer_lastname, customer_age, customer_phone)
            result = customer.rent_bike(rental_shop, bike_ids, rental_type, rental_time)
            print(result)

        elif user_choice == "3":
            bike_ids = input("Enter the bike numbers you want to return (e.g., 1 3 5): ").split()
            bike_ids = [int(bike_id) for bike_id in bike_ids]
            rentals_number = int(input("How many rentals have you performed? "))
            rental_type = input("Enter rental type (hourly, daily, weekly): ")
            rental_time = int(input("Enter rental time: "))

            customer_name = input("Enter your first name: ")
            customer_lastname = input("Enter your last name: ")
            customer_age = int(input("Enter your age: "))
            customer_phone = input("Enter your phone number: ")

            customer = Customer(customer_name, customer_lastname, customer_age, customer_phone)
            result = customer.return_bike(rental_shop, bike_ids, rentals_number, rental_type, rental_time)
            print(result)

        elif user_choice == "4":
            print("Thank you for using the Bike Rental System. Goodbye!")
            break

        else:
            print("Error: Invalid input. Please try again.")

