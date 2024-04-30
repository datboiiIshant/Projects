import mysql.connector

class CreditCardValidator:
    def __init__(self, card_number):
        self.card_number = card_number.replace(" ", "")  # Remove spaces if any
        self.valid = self.validate()

    def validate(self):
        # Check if the card number is composed only of digits
        if not self.card_number.isdigit():
            return False

        # Check if the card number is of valid length
        if len(self.card_number) < 13 or len(self.card_number) > 16:
            return False

        # Perform Luhn's algorithm for checksum validation
        digits = list(map(int, self.card_number))
        checksum = sum(digits[-1::-2]) + sum(sum(divmod(d * 2, 10)) for d in digits[-2::-2])
        return checksum % 10 == 0

    def get_card_type(self):
        # Determine the card type based on the first few digits
        if self.card_number.startswith("4"):
            return "Visa"
        elif self.card_number.startswith("5"):
            return "MasterCard"
        elif self.card_number.startswith(("34", "37")):
            return "American Express"
        elif self.card_number.startswith("6"):
            return "Discover"
        else:
            return "Unknown"

    def is_valid(self):
        return self.valid


def get_credit_card_numbers_from_db():
    # Connect to MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="8560229",
        database="CreditCard"
    )
    cursor = db.cursor()

    # Execute query to fetch all credit card numbers from the database table
    cursor.execute("SELECT card_number FROM credit_cards")  # Modify the query as needed
    results = cursor.fetchall()
    db.close()

    # Return a list of credit card numbers fetched from the database
    return [result[0] for result in results] if results else []


def main():
    # Get all credit card numbers from the database
    credit_card_numbers = get_credit_card_numbers_from_db()

    if credit_card_numbers:
        for card_number in credit_card_numbers:
            validator = CreditCardValidator(card_number)

            if validator.is_valid():
                print(f"Valid {validator.get_card_type()} card: {card_number}")
            else:
                print(f"Invalid card number: {card_number}")
    else:
        print("No credit card numbers found in the database.")

if __name__ == "__main__":
    main()

