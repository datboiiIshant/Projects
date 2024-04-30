import random
import mysql.connector

def generate_credit_card_number(card_type):
    # Define lengths for different card types
    lengths = {
        "visa": 16,
        "mastercard": 16,
        "american express": 15,
        "discover": 16
    }

    # Define prefixes for different card types
    prefixes = {
        "visa": "4",
        "mastercard": random.choice(["51", "52", "53", "54", "55"]),
        "american express": random.choice(["34", "37"]),
        "discover": "6011"
    }

    # Generate random digits for the card number (excluding the checksum digit)
    remaining_digits = ''.join(random.choice('0123456789') for _ in range(lengths[card_type] - len(prefixes[card_type]) - 1))

    # Construct the candidate credit card number
    card_number_candidate = prefixes[card_type] + remaining_digits

    # Calculate the checksum using Luhn's algorithm
    checksum = sum(int(digit) * (2 - i % 2) % 9 for i, digit in enumerate(card_number_candidate[::-1]))
    checksum_digit = (10 - checksum) % 10

    # Construct the complete credit card number
    card_number = card_number_candidate + str(checksum_digit)

    return card_number

def insert_into_mysql(card_type, num_cards):
    # Connect to MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="8560229",
        database="CreditCard"
    )
    cursor = db.cursor()

    # Generate and insert credit card numbers
    for _ in range(num_cards):
        card_number = generate_credit_card_number(card_type)
        sql = "INSERT INTO credit_cards (card_number, card_type) VALUES (%s, %s)"
        val = (card_number, card_type)
        cursor.execute(sql, val)

    # Commit changes and close connection
    db.commit()
    db.close()

    print(f"{num_cards} credit card numbers of type '{card_type}' inserted into MySQL database.")


def main():
    # Generate random card types
    card_types = random.choices(["visa", "mastercard", "american express", "discover"], k=5)  # Generate 5 random card types
    num_cards = 50  # Generate 50 credit card numbers for each type

    # Insert credit card numbers for each random card type
    for card_type in card_types:
        insert_into_mysql(card_type, num_cards)


if __name__ == "__main__":
    main()
